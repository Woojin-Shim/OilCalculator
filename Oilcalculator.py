import customtkinter as ctk

def calculate_density_from_specific_gravity(specific_gravity, reference_density=1000):
    """
    비중을 밀도로 변환하는 함수
    :param specific_gravity: 비중
    :param reference_density: 기준 밀도 (kg/m^3), 기본값은 물의 밀도 1000 kg/m^3
    :return: 밀도 (kg/m^3)
    """
    return specific_gravity * reference_density

def calculate_density_at_temperature(density_at_reference, temperature, reference_temperature=15):
    """
    온도에 따른 밀도 변화를 계산하는 함수
    :param density_at_reference: 기준 온도에서의 밀도 (kg/m^3)
    :param temperature: 현재 온도 (°C)
    :param reference_temperature: 기준 온도 (°C), 기본값은 15°C
    :return: 현재 온도에서의 밀도 (kg/m^3)
    """
    # 여기서는 간단한 선형 관계를 가정합니다. 실제로는 더 복잡한 함수가 필요할 수 있습니다.
    thermal_expansion_coefficient = 0.00064  # 예시로 사용된 열팽창 계수
    delta_temperature = temperature - reference_temperature
    density_at_temperature = density_at_reference / (1 + thermal_expansion_coefficient * delta_temperature)
    return density_at_temperature

def calculate_bunker():
    try:
        temperature = float(entry_temperature.get())
        specific_gravity = float(entry_specific_gravity.get())
        volume = float(entry_volume.get())
        
        # 비중을 밀도로 변환
        density_at_reference = calculate_density_from_specific_gravity(specific_gravity)
        
        # 온도에 따른 밀도 계산
        density_at_temperature = calculate_density_at_temperature(density_at_reference, temperature)
        
        # 무게 계산 (kg)
        weight_in_kg = volume * density_at_temperature
        
        # 메트릭 톤으로 변환
        weight_in_metric_ton = weight_in_kg / 1000  # 1 metric ton = 1000 kg
        
        result_label.configure(text=f"연료의 무게는 {weight_in_metric_ton:.2f} metric ton 입니다.")
    except ValueError:
        result_label.configure(text="유효한 숫자를 입력하세요.")

# 테마 설정
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# 메인 윈도우 생성
root = ctk.CTk()
root.title("벙커 계산기")
root.geometry("300x400")

# 프레임 생성
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# 라벨 및 입력 필드 생성
label_temperature = ctk.CTkLabel(master=frame, text="온도 (°C):")
label_temperature.pack(pady=12, padx=10)
entry_temperature = ctk.CTkEntry(master=frame, placeholder_text="온도 입력")
entry_temperature.pack(pady=12, padx=10)

label_specific_gravity = ctk.CTkLabel(master=frame, text="비중:")
label_specific_gravity.pack(pady=12, padx=10)
entry_specific_gravity = ctk.CTkEntry(master=frame, placeholder_text="비중 입력")
entry_specific_gravity.pack(pady=12, padx=10)

label_volume = ctk.CTkLabel(master=frame, text="부피 (m^3):")
label_volume.pack(pady=12, padx=10)
entry_volume = ctk.CTkEntry(master=frame, placeholder_text="부피 입력")
entry_volume.pack(pady=12, padx=10)

# 계산 버튼 생성
calculate_button = ctk.CTkButton(master=frame, text="계산", command=calculate_bunker)
calculate_button.pack(pady=12, padx=10)

# 결과 표시 라벨 생성
result_label = ctk.CTkLabel(master=frame, text="")
result_label.pack(pady=12, padx=10)

# 메인 루프 실행
root.mainloop()