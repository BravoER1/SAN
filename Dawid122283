#include <stdio.h>
#include <stdlib.h>
#include <windows.h>


float a,b,operacja,suma,roznica,iloczyn,iloraz;
int i,c;



int main() 
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

	puts("\t\t\t\t\t##########################");   
	puts("\t\t\t\t\t\tKALKULATOR\t\t\t\t\n\t\t\t\t\t##########################\n\n");
	printf("Nacisnij dowolny klawisz, aby rozpoczac.");
	poczatek:
	getchar();
	sleep(2);
	
	printf("\nWybierz operacje, ktora chcesz wykonac:\n\n1-dodawanie\n2-odejmowanie\n3-mnozenie\n4-dzielenie\n\n");
	printf("Podaj numer operacji: ");
	scanf("%f",&operacja);
	
	dzielenie:
		
	
	if(operacja==1)
		{
			printf("\nPodaj pierwsza liczbe: ");
			scanf("%f",&a);
			printf("Podaj druga liczbe: ");
			scanf("%f",&b);
			printf("\nDODAWANIE W TOKU\n");
				for(i=0;i<5;i++)
						{
							fflush(stdout);
							sleep(1);
							printf("###");
						}
			suma = a+b;
			printf("\n\nSuma podanych liczb wynosi: %.2f",suma);
		}
			else if(operacja==2)
				{	printf("\nPodaj pierwsza liczbe: ");
					scanf("%f",&a);
					printf("Podaj druga liczbe: ");
					scanf("%f",&b);
					printf("\nODEJMOWANIE W TOKU\n");
						for(i=0;i<5;i++)
						{
							fflush(stdout);
							sleep(1);
							printf("###");
						}
					roznica=a-b;
					printf("\n\nRoznica podanych liczb wynosi: %.2f",roznica);
 			}
				else if(operacja==3)
				{	printf("\nPodaj pierwsza liczbe: ");
					scanf("%f",&a);
					printf("Podaj druga liczbe: ");
					scanf("%f",&b);
					printf("\nMNOZENIE W TOKU\n");
						for(i=0;i<5;i++)
						{
							fflush(stdout);
							sleep(1);
							printf("###");
						}
					iloczyn = a*b;
					printf("\n\nIloczyn podanych liczb wynosi: %.2f",iloczyn);
				}
					
					else if(operacja==4)
				{	printf("\nPodaj pierwsza liczbe: ");
					scanf("%f",&a);
					printf("Podaj druga liczbe: ");
					scanf("%f",&b);
					printf("\nDZIELENIE W TOKU\n");
						for(i=0;i<5;i++)
						{
							fflush(stdout);
							sleep(1);
							printf("###");
						}
					
						if(a == 0 || b == 0)
						{
							SetConsoleTextAttribute(hConsole,FOREGROUND_RED);
							puts("\n\nNie dziel przez zero !");
							SetConsoleTextAttribute(hConsole,FOREGROUND_RED |FOREGROUND_GREEN | FOREGROUND_BLUE);
							puts("\nNacisnij dowolny przycisk, aby powrocic do ekranu dzielenia");
							while ((c = getchar()) != '\n' && c != EOF){}
							getchar();
							goto dzielenie;
						}
						else 
						iloraz=a/b;
					
					printf("\n\nIloraz podanych liczb wynosi: %.2f",iloraz);
					
				}
					else
					{
						puts("\nWprowadziles bledna wartosc operacji !\n");
						goto poczatek;
					}
					return 0;
				}
			


