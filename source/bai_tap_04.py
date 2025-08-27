import random

print('----- Trò chơi đoán số -----')
print('Bạn có sẵn 100$ tiền chơi')

user_money = 100
win_game = 0
lose_game = 0
playagain = "Yes"

while (playagain == 'Yes' or playagain == 'yes') and user_money >= 5:
    print('\nMáy tính đang nghĩ một con số từ 1 đến 100...')
    comp_num = random.randint(1, 100)
    user = 'You lose'  # Giả định ban đầu là thua

    for i in range(5):
        try:
            user_num = int(input(f'Lần {i+1} - Nhập một số từ 1 đến 100: '))
        except ValueError:
            print("⚠️ Lỗi: Bạn phải nhập một **số nguyên hợp lệ**.")
            continue

        if user_num < 1 or user_num > 100:
            print("⚠️ Số bạn nhập ngoài phạm vi! Vui lòng chọn từ 1 đến 100.")
            continue

        if comp_num == user_num:
            print('🎉 Bạn đã đoán đúng! Bạn thắng ván này.')
            user = 'You win'
            break
        elif comp_num > user_num:
            print("🔻 Số bạn đoán NHỎ HƠN số của máy.")
        else:
            print("🔺 Số bạn đoán LỚN HƠN số của máy.")

    # Kết thúc ván chơi, cập nhật kết quả
    if user == 'You win':
        win_game += 1
        user_money += 5
    else:
        lose_game += 1
        user_money -= 5
        print(f'❌ Bạn đã thua ván này! Số đúng là: {comp_num}')

    print(f'💰 Số tiền còn lại của bạn: {user_money}$')

    if user_money >= 5:
        playagain = input('Bạn có muốn chơi tiếp không? [Yes/No]: ')
    else:
        print('🚫 Bạn đã hết tiền cược!')

# Kết thúc trò chơi, in báo cáo
print('\n----- Báo cáo tổng kết -----')
print(f'💰 Tổng số tiền còn lại: {user_money}$')
print(f'✅ Số ván thắng: {win_game}')
print(f'❌ Số ván thua: {lose_game}')
print('🎮 Cảm ơn bạn đã chơi!')
