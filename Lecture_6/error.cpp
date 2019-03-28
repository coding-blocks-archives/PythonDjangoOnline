#include <iostream>
using namespace std;

class Exception {
				public:
								char message[20]	= "Error";
};

int main() {
				try {
								throw 1;
				} catch (int i){
								cout << "Error occured";
				}

				return 0;
}
