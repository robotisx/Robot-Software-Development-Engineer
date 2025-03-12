import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(theta1, theta2, theta3, l1=1.5, l2=1.2, l3=0.8):
    """
    3자유도 로봇 팔의 순방향 기구학을 계산하는 함수
    """
    # 각도를 라디안으로 변환
    theta1 = np.radians(theta1)
    theta2 = np.radians(theta2)
    theta3 = np.radians(theta3)
    
    # 링크 끝점 좌표 계산
    x1, y1 = l1 * np.cos(theta1), l1 * np.sin(theta1)
    x2, y2 = x1 + l2 * np.cos(theta1 + theta2), y1 + l2 * np.sin(theta1 + theta2)
    x3, y3 = x2 + l3 * np.cos(theta1 + theta2 + theta3), y2 + l3 * np.sin(theta1 + theta2 + theta3)
    
    positions = [(0, 0), (x1, y1), (x2, y2), (x3, y3)]
    
    # 좌표 출력
    print("Link Positions:")
    for i, (x, y) in enumerate(positions):
        print(f"Joint {i}: ({x:.2f}, {y:.2f})")
    
    return positions, (x3, y3)

def plot_robot_arm(positions, end_effector):
    """
    로봇 팔을 시각화하는 함수
    """
    x_vals, y_vals = zip(*positions)
    
    plt.figure(figsize=(6, 6))

    # 각 링크의 색상을 다르게 설정 (링크 1은 빨강, 링크 2는 파랑, 링크 3은 초록)
    plt.plot(x_vals[:2], y_vals[:2], 'o-', markersize=8, linewidth=5, color='red', label='Link 1')  # 첫 번째 링크
    plt.plot(x_vals[1:3], y_vals[1:3], 'o-', markersize=8, linewidth=5, color='blue', label='Link 2')  # 두 번째 링크
    plt.plot(x_vals[2:], y_vals[2:], 'o-', markersize=8, linewidth=5, color='green', label='Link 3')  # 세 번째 링크

    # 관절 (각 조인트) 색상 다르게 설정 (각각의 관절을 검정색 점으로 표시)
    for i, (x, y) in enumerate(positions):
        plt.scatter(x, y, color='black', s=100, zorder=5)  # 관절을 검정색 점으로 표시
    

    x_end, y_end = end_effector

    # 각 조인트 좌표 텍스트 추가
    for i, (x, y) in enumerate(positions):
        plt.text(x, y, f' {i}', fontsize=12, fontweight='bold', verticalalignment='bottom', horizontalalignment='right', color='black')
    
    # 엔드 이펙터 좌표 텍스트 추가
    plt.text(x_end, y_end, f'({x_end:.2f}, {y_end:.2f})', fontsize=12, fontweight='bold', color='blue', verticalalignment='bottom')

    # 1사분면으로 그래프 제한
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("3-DOF Robot Arm Visualization")
    plt.show()


theta1, theta2, theta3 = 15, 20, 30 #[deg]
positions, end_effector = forward_kinematics(theta1, theta2, theta3)
plot_robot_arm(positions, end_effector)
