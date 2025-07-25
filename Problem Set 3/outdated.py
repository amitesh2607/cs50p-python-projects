months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if date[0].isalpha():

            date = (date.split(","))
            month_str, day = date[0].split()
            year = date[1]
            month = months.index(month_str) + 1
        else:

            month, day, year = date.split("/")
            month = int(month)

        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
            break

    except (ValueError, IndexError):
        continue


print(f"{year}-{month:02}-{day:02}")




