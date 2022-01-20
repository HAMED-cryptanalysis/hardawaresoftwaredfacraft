
#include <avr/io.h>
#include <util/delay.h>
#include "global.h"

int main(void)
{

	sbi(DDRB,0);
	cbi(PORTB,0);
	sbi(DDRB,1);
	cbi(PORTB,1);

	while (TRUE)
	{
		sbi(PORTB,0);
		cbi(PORTB,0);

	}
}