# 문제 1.
#
# 서보모터 각도를 PWM pulse width 값으로 변환하세요.
#
# angle 값은 0 ~ 180 범위입니다.
#
# 0도   -> 500
# 90도  -> 1500
# 180도 -> 2500
#
# 선형 비례 관계로 계산하세요.
def servo_angle_to_pulse_width(angle):
    return (1000 * angle // 90) + 500


# 문제 2.
#
# 부저로 출력할 음계 이름을 주파수 값으로 변환하세요.
#
# C4, D4, E4, F4, G4, A4, B4, C5 음계를 지원해야 합니다.
def note_to_frequency(note):
    notes = {
    "C4": 262,  # C4
    "D4": 294,  # D4
    "E4": 330,  # E4
    "F4": 349,  # F4
    "G4": 392, # G4
    "A4": 440,  # A4
    "B4": 494,  # B4
    "C5": 523,  # C5
    }
    if note in notes:
        return notes[note]
    else:
        return 0


# 문제 3.
#
# 여러 개의 음계를 부저 주파수 리스트로 변환하세요.
#
# notes 인자는 음계 이름이 들어있는 리스트입니다.
# 각 음계를 주파수 값으로 변환한 리스트를 반환하세요.
def melody_to_frequencies(notes):
    m_to_freq = {
    "C4": 262,  # C4
    "D4": 294,  # D4
    "E4": 330,  # E4
    "F4": 349,  # F4
    "G4": 392, # G4
    "A4": 440,  # A4
    "B4": 494,  # B4
    "C5": 523,  # C5
    }
    note_list = []
    for note in notes:
        note_list.append(m_to_freq[note])
    return note_list


# 문제 4.
#
# 로봇 이동 방향 문자열을 ROS2 Twist 값으로 변환하세요.
#
# direction 인자는 이동 방향 문자열입니다.
#
# 지원해야 하는 방향은 아래와 같습니다.
#
# - forward
# - backward
# - left
# - right
# - stop
#
# 반환값은 (linear_x, angular_z) 튜플입니다.
def direction_to_twist(direction):
    match direction:
        case "forward": return (1.0, 0.0)
        case "backward": return (-1.0, 0.0)
        case "left": return (0.0, 1.0)
        case "right":return (0.0, -1.0)
        case _ : return (0.0, 0.0)


# 문제 5.
#
# ROS2 Twist 값을 좌우 바퀴 속도로 변환하세요.
#
# linear_x는 전진/후진 속도입니다.
# angular_z는 회전 속도입니다.
#
# 좌우 바퀴 속도는 -100 ~ 100 범위로 제한되어야 합니다.
#
# 반환값은 (left_speed, right_speed) 튜플입니다.
def twist_to_wheel_speed(linear_x, angular_z):
    left = (linear_x - angular_z) * 100
    right = (linear_x + angular_z) * 100

    left = max(-100, min(100, left))
    right = max(-100, min(100, right))

    return int(left), int(right)
