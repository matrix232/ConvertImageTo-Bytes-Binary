# Menu for choose
import Convert


class MenuConverter:

    def __init__(self, select: str):
        self.select = select

    def Select(self):
        try:
            if self.select == "0":
                print("EXIT...")
            elif self.select == "1":
                path = input("Enter path to picture: ")
                con = Convert.convert(path)
                con.ImageToBytes()
            elif self.select == "2":
                path = input("Enter path to bytes: ")
                con = Convert.convert(path)
                con.BytesToImage()
            elif self.select == "3":
                path = input("Enter path to picture: ")
                con = Convert.convert(path)
                con.ImageToBinary()
            elif self.select == "4":
                path = input("Enter path to binary code: ")
                con = Convert.convert(path)
                con.BinaryToImage()
            else:
                print("INVALID OPERATOR!")

        except TypeError:
            print("NOT FOUND!")


if __name__ == "__main__":
    convert = MenuConverter(select=input(
        "0-exit; 1-convert image to bytes; 2-convert bytes to image; 3-convert image to binary; 4-convert binary to image: "))

    convert.Select()
