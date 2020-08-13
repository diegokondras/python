#!/usr/bin/python3

###
## Exercicios
###

#1) Crie uma lista com os 1000 primeiros numeros pares.
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		ArrayList<Integer> a = new ArrayList<>();
		int cont  = 0;
		while(a.size() != 1000) {
			if (cont%2 == 0) 
				a.add(cont);	
			cont++;
		}
	}

}


#2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		ArrayList<Integer> a = new ArrayList<>();
		
		for(int i=0; i<=99999999999999999999999999; i++) {
			a.add(i);
		}
		
		for(int num : a) {
			if (num%5 == 0) {
				System.out.println(num);
				break;
			}
		}
		
	}

}