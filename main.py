import speedtest


st = speedtest.Speedtest()
option = int(input('''
Выбери тип проверки:   

1 - Скорость скачивания   
2 - Скорость загрузки   
3 - Пинг
4 - все вместе
Твой выбор: '''))


if option == 1:
    print(f"Скачивание: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
elif option == 2:
    print(f"Загрузка: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(f"Пинг: {st.results.ping}")
elif option == 4:
    print(f"Скачивание: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
    print(f"Загрузка: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")
    print(f"Пинг: {st.results.ping}")
else:
    print("Пожалуйста, введите цифру от 1 до 4!")
