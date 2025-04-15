def calculate_failure_load(temp_celsius, thickness_m, void_radius_m):
    # 상수값
    E_20 = 5_000 * 1e6   # 5000 MPa -> Pa
    k_shape = 1.33       # 형상 계수
    k_temp = 0.05        # 온도 민감도
    correction_factor = 0.3  # 보정 계수

    # 온도에 따른 탄성계수 계산
    E_temp = E_20 * (10 ** (-k_temp * (temp_celsius - 20)))

    # 파괴하중 계산 (단위: N)
    P_newton = (k_shape * E_temp * (thickness_m ** 3)) / (void_radius_m ** 2) * correction_factor

    # 단위를 kgf로 변환하고 반올림
    P_kgf = round(P_newton / 9.81)

    return P_kgf

# 무한 반복
while True:
    print("\n📌 아스팔트 파괴하중 계산기 (종료하려면 'q' 입력)")
    try:
        temp_input = input("아스팔트 온도(℃)를 입력하세요: ")
        if temp_input.lower() == 'q':
            print("프로그램을 종료합니다. 😊")
            break

        thickness_input = input("아스팔트 두께(m)를 입력하세요 (예: 0.08): ")
        if thickness_input.lower() == 'q':
            print("프로그램을 종료합니다. 😊")
            break

        radius_input = input("공동의 반지름(m)를 입력하세요: ")
        if radius_input.lower() == 'q':
            print("프로그램을 종료합니다. 😊")
            break

        # 숫자 변환
        temp = float(temp_input)
        thickness = float(thickness_input)
        radius = float(radius_input)

        # 결과 출력
        result = calculate_failure_load(temp, thickness, radius)
        print(f"\n✅ 아스팔트 파괴하중: {result} kgf")

    except ValueError:
        print("❌ 숫자 형식으로 정확히 입력해주세요!")
