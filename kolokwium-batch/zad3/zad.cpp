#include <fstream>
#include <iostream>

using namespace std;
  
int main(int argc, char* argv[]){

    string linia;
    int slowa = 1;
    fstream plik;
    
	plik.open(argv[1], std::ios::in | std::ios::out);
	
	if( plik.good() == true ){
		while(plik.good() && getline(plik, linia, '\n')){
        	int l=linia.length();
            
        	for (int i=0;i<l;i++){
        		if (isspace(linia[i])) slowa++;
    		}   		
        }
        cout<<slowa;
        plik.close();
	} 
	//else cout << "Nie otworzono pliku";
	
	return 0;
}
