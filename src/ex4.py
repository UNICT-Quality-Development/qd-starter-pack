# Surprise me.
#
# #include <stdio.h>
#
# int main()
# {
#   int month;
#
#   /* Input month number from user */
#   printf("Enter month number(1-12): ");
#   scanf("%d", &month);
#
#   switch (month)
#   {
#   case 1:
#     printf("31 days");
#     break;
#   case 2:
#     printf("28/29 days");
#     break;
#   case 3:
#     printf("31 days");
#     break;
#   case 4:
#     printf("30 days");
#     break;
#   case 5:
#     printf("31 days");
#     break;
#   case 6:
#     printf("30 days");
#     break;
#   case 7:
#     printf("31 days");
#     break;
#   case 8:
#     printf("31 days");
#     break;
#   case 9:
#     printf("30 days");
#     break;
#   case 10:
#     printf("31 days");
#     break;
#   case 11:
#     printf("30 days");
#     break;
#   case 12:
#     printf("31 days");
#     break;
#   default:
#     printf("Invalid input! Please enter month number between 1-12");
#   }
#
#   return 0;
# }


def main():
    month = int(input("Enter month number(1-12): "))

    match(month):
        case 1:
            print("31 days")
        case 2:
            print("28/29 days")
        case 3:
            print("31 days")
        case 4:
            print("30 days")
        case 5:
            print("31 days")
        case 6:
            print("30 days")
        case 7:
            print("31 days")
        case 8:
            print("31 days")
        case 9:
            print("30 days")
        case 10:
            print("31 days")
        case 11:
            print("30 days")
        case 12:
            print("31 days")
        case _:
            print("Invalid input! Please enter month number between 1-12")


if __name__ == "__main__":
    main()
