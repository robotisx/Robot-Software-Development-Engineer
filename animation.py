import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def forward_kinematics(theta1, theta2, theta3, l1=1.5, l2=1.5, l3=1.5):
    theta1, theta2, theta3 = np.radians([theta1, theta2, theta3])
    
    x1, y1 = l1 * np.cos(theta1), l1 * np.sin(theta1)
    x2, y2 = x1 + l2 * np.cos(theta1 + theta2), y1 + l2 * np.sin(theta1 + theta2)
    x3, y3 = x2 + l3 * np.cos(theta1 + theta2 + theta3), y2 + l3 * np.sin(theta1 + theta2 + theta3)
    
    return [(0, 0), (x1, y1), (x2, y2), (x3, y3)], (x3, y3), theta1 + theta2 + theta3

# 화면 설정
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True, linestyle="--", alpha=0.6)

# 로봇 팔을 그리는 요소
line, = ax.plot([], [], 'o-', markersize=8, linewidth=5, color='black')  # 로봇 팔
path_line, = ax.plot([], [], 'r-', linewidth=2, alpha=0.7)  # 엔드 이펙터 궤적
gripper_left, = ax.plot([], [], 'b-', linewidth=3)  # 왼쪽 그리퍼
gripper_right, = ax.plot([], [], 'b-', linewidth=3)  # 오른쪽 그리퍼
gripper_bottom, = ax.plot([], [], 'b-', linewidth=3)  # 바닥 부분 "_"
joint_texts = [ax.text(0, 0, "", fontsize=12, fontweight='bold', color='red') for _ in range(3)]  # 각도 표시
end_effector_text = ax.text(0, 0, "", fontsize=12, fontweight='bold', color='blue')  # 엔드 이펙터 좌표 표시

# 엔드 이펙터 궤적 저장 리스트
end_effector_path = []

# 애니메이션 업데이트 함수
def animate(i):
    # 실제 로봇 팔처럼 부드럽게 움직이도록 설정
    theta1 = 20 + 20 * np.sin(np.radians(i * 3))  # 0도 ~ 40도 사이 진동
    theta2 = 30 + 15 * np.sin(np.radians(i * 2))  # 15도 ~ 45도 사이 진동
    theta3 = -20 + 25 * np.sin(np.radians(i * 4)) # -45도 ~ 5도 사이 진동
    
    positions, end_effector, theta_total = forward_kinematics(theta1, theta2, theta3)
    x_vals, y_vals = zip(*positions)
    
    # 로봇 팔 업데이트
    line.set_data(x_vals, y_vals)

    # 엔드 이펙터 궤적 저장 및 업데이트
    end_effector_path.append(end_effector)  # 궤적 리스트에 추가
    path_x, path_y = zip(*end_effector_path)  # 리스트에서 X, Y 좌표 분리
    path_line.set_data(path_x, path_y)  # 궤적 업데이트
    
    # 각 링크별 각도 표시
    angles = [theta1, theta2, theta3]
    for j in range(3):
        joint_texts[j].set_position((x_vals[j], y_vals[j]))
        joint_texts[j].set_text(f"{angles[j]:.1f}°")
    
    # 엔드 이펙터 좌표 표시 (잘리지 않도록 위치 조정)
    end_effector_text.set_position((end_effector[0], end_effector[1]))
    end_effector_text.set_text(f"({end_effector[0]:.2f}, {end_effector[1]:.2f})")

    # === "ㄷ" 모양의 그리퍼 추가 ===
    gripper_length = 0.3  # 그리퍼 세로 길이
    gripper_width = 0.2   # 그리퍼 폭
    bottom_width = 0.4    # 바닥 "_" 부분 폭

    # 회전 행렬을 사용하여 그리퍼 위치 계산
    cos_t, sin_t = np.cos(theta_total), np.sin(theta_total)
    
    # 왼쪽, 오른쪽 그리퍼 좌표 (엔드 이펙터를 감싸는 구조)
    left_x1 = end_effector[0] - gripper_width * sin_t
    left_y1 = end_effector[1] + gripper_width * cos_t
    left_x2 = left_x1 - gripper_length * cos_t
    left_y2 = left_y1 - gripper_length * sin_t

    right_x1 = end_effector[0] + gripper_width * sin_t
    right_y1 = end_effector[1] - gripper_width * cos_t
    right_x2 = right_x1 - gripper_length * cos_t
    right_y2 = right_y1 - gripper_length * sin_t

    # 바닥 "_" 부분 좌표 (ㄷ 모양의 아랫부분)
    bottom_x1 = left_x2
    bottom_y1 = left_y2
    bottom_x2 = right_x2
    bottom_y2 = right_y2

    # 그리퍼 업데이트
    gripper_left.set_data([left_x1, left_x2], [left_y1, left_y2])
    gripper_right.set_data([right_x1, right_x2], [right_y1, right_y2])
    gripper_bottom.set_data([bottom_x1, bottom_x2], [bottom_y1, bottom_y2])  # "_" 부분 중앙 정렬

    return [line, path_line, gripper_left, gripper_right, gripper_bottom] + joint_texts + [end_effector_text]

# 애니메이션 실행
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50, blit=True)
plt.title("3-DOF Robot Arm Animation")
plt.show()
