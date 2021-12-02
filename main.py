from wiegand import Wiegand
from machine import Pin
import time

WIEGAND_ZERO = 4  
WIEGAND_ONE = 5

KNOWN_CARD_ID = <CARD_ID_HERE>

def on_card(card_number, facility_code, cards_read):
    print(card_number,facility_code,cards_read)
    if card_number == KNOWN_CARD_ID:

        #blink the led if the card id is known
        p0 = Pin(2, Pin.OUT)
        p0.off()
        time.sleep_ms(500)
        p0.on()

    
Wiegand(WIEGAND_ZERO, WIEGAND_ONE, on_card)
