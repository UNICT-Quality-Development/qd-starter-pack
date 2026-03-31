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
# Mese -> numero di giorni
giorni_del_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    mese = int(input("Inserisci il numero del mese (1-12): "))
    if 1 <= mese <= 12:
        print(f"Il mese {mese} ha {giorni_del_mese[mese - 1]} giorni.")
    else:
        print("Input non valido! Inserisci un numero tra 1 e 12.")
except ValueError:
    print("Input non valido! Inserisci un numero intero valido.")
