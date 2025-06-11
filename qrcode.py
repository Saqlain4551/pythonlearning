import qrcode

github_repo = input("Enter your GitHub repository (username/repository): ")
github_url = f'https://github.com/{github_repo}'

try:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(github_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('github_qr.png')
    img.show()
except Exception as e:
    print(f"An error occurred: {e}")
