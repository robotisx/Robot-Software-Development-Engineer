# Robot-Software-Development-Engineer
로봇소프트웨어개발기사 실습 코드입니다. 유튜브에 로코딩을 검색하시면 로봇소프트웨어개발기사 실기 무료강의를 볼 수 있습니다.

```markdown
### 로봇 팔 시각화 함수 설명

```python
def plot_robot_arm(positions, end_effector):
    """
    로봇 팔을 시각화하는 함수
    """
```
- `plot_robot_arm` 함수는 로봇 팔의 위치와 끝단(End-Effector)을 시각화하는 함수입니다. 
- 입력으로 `positions` (각 관절의 좌표)과 `end_effector` (엔드 이펙터의 좌표)를 받습니다.

```python
    x_vals, y_vals = zip(*positions)
```
- `positions` 리스트에서 각 관절의 x, y 좌표를 분리하여 `x_vals`와 `y_vals`에 저장합니다.
- `zip(*positions)`은 `positions`의 각 튜플을 풀어서 x와 y 좌표를 각각 따로 분리합니다.

```python
    plt.figure(figsize=(6, 6))
```
- `plt.figure()`는 새로운 그래프를 생성하며, `figsize=(6, 6)`는 그래프의 크기를 6x6인치로 설정합니다.

```python
    plt.plot(x_vals[:2], y_vals[:2], 'o-', markersize=8, linewidth=5, color='red', label='Link 1')  # 첫 번째 링크
```
- `plt.plot()`은 첫 번째 링크를 그립니다. `x_vals[:2]`와 `y_vals[:2]`는 첫 번째 관절과 두 번째 관절을 연결하는 좌표입니다.
- `'o-'`는 원형 마커와 선으로 연결을 의미하고, `markersize=8`은 마커의 크기를 8로 설정합니다.
- `linewidth=5`는 선의 두께를 5로 설정하고, `color='red'`는 선의 색을 빨간색으로 지정합니다.
- `label='Link 1'`은 첫 번째 링크에 대한 레이블을 추가합니다.

```python
    plt.plot(x_vals[1:3], y_vals[1:3], 'o-', markersize=8, linewidth=5, color='blue', label='Link 2')  # 두 번째 링크
```
- 두 번째 링크를 그립니다. `x_vals[1:3]`와 `y_vals[1:3]`는 두 번째 관절과 세 번째 관절을 연결하는 좌표입니다.
- 선의 색은 파란색(`color='blue'`)이고, 마커와 선은 빨간 링크와 동일한 스타일입니다.

```python
    plt.plot(x_vals[2:], y_vals[2:], 'o-', markersize=8, linewidth=5, color='green', label='Link 3')  # 세 번째 링크
```
- 세 번째 링크를 그립니다. `x_vals[2:]`와 `y_vals[2:]`는 세 번째 관절과 엔드 이펙터를 연결하는 좌표입니다.
- 선의 색은 초록색(`color='green'`)으로 설정됩니다.

```python
    for i, (x, y) in enumerate(positions):
        plt.scatter(x, y, color='black', s=100, zorder=5)  # 관절을 검정색 점으로 표시
```
- 각 관절의 위치에 대해 검정색 점(`scatter`)을 그립니다. 
- `x`와 `y`는 각 관절의 좌표이고, `color='black'`은 점의 색을 검정색으로, `s=100`은 점의 크기를 100으로 설정합니다.
- `zorder=5`는 점이 다른 그래프 요소들보다 위에 표시되도록 합니다.

```python
    # 엔드 이펙터 강조 (빨간색으로 표시)
    x_end, y_end = end_effector
```
- 엔드 이펙터의 좌표를 `x_end`, `y_end`로 분리합니다.

```python
    # plt.scatter(x_end, y_end, color='red', s=200, edgecolors='black', linewidth=2, label='End-Effector')  
```
- 주석 처리된 부분은 엔드 이펙터를 빨간색으로 강조하는 코드입니다.
- 현재 주석 처리되어 있지만, 이 코드를 활성화하면 엔드 이펙터가 빨간색으로 표시됩니다.

```python
    for i, (x, y) in enumerate(positions):
        plt.text(x, y, f' {i}', fontsize=12, fontweight='bold', verticalalignment='bottom', horizontalalignment='right', color='black')
```
- 각 관절에 텍스트를 추가하여 관절의 번호를 표시합니다. `i`는 관절의 인덱스 번호입니다.
- 텍스트 크기(`fontsize=12`), 두껍게(`fontweight='bold'`), 텍스트 위치 조정(`verticalalignment='bottom'`, `horizontalalignment='right'`) 등을 설정합니다.

```python
    plt.text(x_end, y_end, f'({x_end:.2f}, {y_end:.2f})', fontsize=12, fontweight='bold', color='blue', verticalalignment='bottom')
```
- 엔드 이펙터의 좌표를 텍스트로 표시합니다. 좌표를 소수점 두 자릿수로 출력하며(`{x_end:.2f}`), 텍스트 색상은 파란색(`color='blue'`)으로 설정됩니다.

```python
    plt.xlim(0, 4)
    plt.ylim(0, 4)
```
- 그래프의 x축과 y축의 범위를 각각 0부터 4로 설정합니다.

```python
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
```
- `axhline(0)`과 `axvline(0)`는 x축과 y축을 0에서 그리는 코드입니다. 축선은 검정색이고, 두께는 0.5로 설정됩니다.

```python
    plt.grid(True, linestyle='--', alpha=0.6)
```
- 그래프에 격자선을 추가합니다. `linestyle='--'`는 대시 선을 사용하고, `alpha=0.6`은 투명도를 60%로 설정합니다.

```python
    plt.legend()
```
- 그래프에 범례를 추가합니다. 각 링크에 대한 레이블을 자동으로 표시합니다.

```python
    plt.title("3-DOF Robot Arm Visualization")
```
- 그래프의 제목을 설정합니다. "3-DOF Robot Arm Visualization"이라고 표시됩니다.

```python
    plt.show()
```
- 최종적으로 그래프를 화면에 표시합니다.
```


코드를 한 줄씩 분석하면서 설명해드릴게요.

---

## **1. 함수 정의 및 입력 매개변수**
```python
def plot_robot_arm(positions, end_effector):
```
- **함수명**: `plot_robot_arm`
- **매개변수**:
  - `positions`: 로봇 팔의 각 관절 위치 리스트 (예: `[(x0, y0), (x1, y1), (x2, y2), (x3, y3)]`)
  - `end_effector`: 엔드 이펙터 (로봇 팔 끝부분) 좌표 `(x3, y3)`

---

## **2. 좌표 데이터 분리**
```python
x_vals, y_vals = zip(*positions)
```
- `positions` 리스트에서 `x`와 `y` 좌표를 각각 분리하여 `x_vals`와 `y_vals`에 저장.
- `zip(*positions)`을 사용하면 각 튜플에서 첫 번째 요소(즉, `x` 좌표)와 두 번째 요소(즉, `y` 좌표)를 분리할 수 있음.

---

## **3. 그래프 크기 설정**
```python
plt.figure(figsize=(6, 6))
```
- 그래프 크기를 **6 x 6 인치**로 설정.

---

## **4. 로봇 팔 각 링크를 색상별로 그림**
```python
plt.plot(x_vals[:2], y_vals[:2], 'o-', markersize=8, linewidth=5, color='red', label='Link 1')  # 첫 번째 링크
plt.plot(x_vals[1:3], y_vals[1:3], 'o-', markersize=8, linewidth=5, color='blue', label='Link 2')  # 두 번째 링크
plt.plot(x_vals[2:], y_vals[2:], 'o-', markersize=8, linewidth=5, color='green', label='Link 3')  # 세 번째 링크
```
- **각 링크의 색상 구분**:
  - **첫 번째 링크** (베이스 ~ 첫 번째 관절): 빨간색 (`red`)
  - **두 번째 링크** (첫 번째 관절 ~ 두 번째 관절): 파란색 (`blue`)
  - **세 번째 링크** (두 번째 관절 ~ 엔드 이펙터): 초록색 (`green`)
- `'o-'`: 각 관절을 **점(`o`)**으로 표시하고, **선(`-`)**으로 연결.
- `markersize=8`: 관절 점의 크기를 8로 설정.
- `linewidth=5`: 선의 두께를 5로 설정.
- `label='Link X'`: 범례에서 링크를 구분할 수 있도록 레이블 추가.

---

## **5. 관절(조인트) 시각화**
```python
for i, (x, y) in enumerate(positions):
    plt.scatter(x, y, color='black', s=100, zorder=5)  # 관절을 검정색 점으로 표시
```
- `positions` 리스트를 순회하며 **각 관절을 검정색(`black`) 점으로 표시**.
- `s=100`: 점의 크기를 100으로 설정.
- `zorder=5`: 다른 그래프 요소보다 위에 그려지도록 설정.

---

## **6. 엔드 이펙터 강조 (현재 코드에서 주석 처리됨)**
```python
# plt.scatter(x_end, y_end, color='red', s=200, edgecolors='black', linewidth=2, label='End-Effector')  
```
- 엔드 이펙터를 **빨간색(`red`) 점**으로 강조하려 했으나, **현재는 주석 처리**되어 있음.
- `edgecolors='black'`: 점의 테두리를 검정색으로 설정.
- `s=200`: 크기를 200으로 설정.

---

## **7. 각 조인트에 번호(인덱스) 추가**
```python
for i, (x, y) in enumerate(positions):
    plt.text(x, y, f' {i}', fontsize=12, fontweight='bold', verticalalignment='bottom', horizontalalignment='right', color='black')
```
- 관절 번호를 텍스트로 추가 (`i`는 0부터 시작).
- `fontsize=12`: 글씨 크기 12.
- `fontweight='bold'`: 글씨를 굵게 표시.
- `verticalalignment='bottom'`, `horizontalalignment='right'`: **텍스트 위치 조정** (조인트의 약간 오른쪽 아래에 표시).
- `color='black'`: 글씨 색상을 검정색으로 설정.

---

## **8. 엔드 이펙터 좌표 표시**
```python
plt.text(x_end, y_end, f'({x_end:.2f}, {y_end:.2f})', fontsize=12, fontweight='bold', color='blue', verticalalignment='bottom')
```
- 엔드 이펙터의 **좌표값을 출력**.
- `(x_end:.2f), (y_end:.2f)`: **소수점 두 자리까지 출력**.
- `color='blue'`: 텍스트 색상을 파란색으로 설정.
- `verticalalignment='bottom'`: 텍스트 위치 조정.

---

## **9. 그래프 설정**
```python
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
```
- **그래프 범위 제한**: \( x, y \) 값이 **0~4 사이**로 설정.
- **축 설정**:
  - `plt.axhline(0)`: \( y = 0 \) 축을 검정색(`black`)으로 표시.
  - `plt.axvline(0)`: \( x = 0 \) 축을 검정색으로 표시.
- **그리드 추가**:
  - `linestyle='--'`: 점선(`--`) 스타일의 격자.
  - `alpha=0.6`: 투명도 60%.

---

## **10. 범례 추가 및 그래프 표시**
```python
plt.legend()
plt.title("3-DOF Robot Arm Visualization")
plt.show()
```
- `plt.legend()`: 범례 표시 (각 링크에 대한 색상 정보를 제공).
- `plt.title()`: 그래프 제목을 **"3-DOF Robot Arm Visualization"**으로 설정.
- `plt.show()`: 그래프를 화면에 출력.

---

### **📌 코드 요약**
1. **입력값(각 관절 위치들)을 받아서 로봇 팔을 시각화**.
2. **각 링크를 다른 색상으로 그려서 구분**.
3. **각 관절을 검정색 점으로 강조**.
4. **각 관절 번호 및 엔드 이펙터 좌표를 표시**.
5. **그래프를 보기 좋게 설정 후 출력**.

이제 이 함수에 `positions`와 `end_effector` 좌표를 전달하면 **3-DOF 로봇 팔의 정적 이미지를 그릴 수 있음**! 🚀
