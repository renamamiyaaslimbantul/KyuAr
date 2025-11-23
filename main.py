import qrcode
import binascii
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
qris_base = os.getenv("QRIS_BASE")
amount = os.getenv("AMOUNT")
amount_field = f"5406{amount.zfill(6)}"  # QRIS format: 54 (amount), 06 (length), 020000 (amount)

# Remove any existing CRC (field 63) if present
import re
qris_no_crc = re.sub(r'6304.{4}$', '', qris_base + amount_field)

# Append CRC field ID and length (but not value yet)
qris_for_crc = qris_no_crc + '6304'

# Calculate CRC-16-CCITT (0x1021) as per QRIS/EMVCo spec
def crc16_ccitt(data: str) -> str:
	crc = 0xFFFF
	for c in data:
		crc ^= ord(c) << 8
		for _ in range(8):
			if crc & 0x8000:
				crc = (crc << 1) ^ 0x1021
			else:
				crc <<= 1
			crc &= 0xFFFF
	return format(crc, '04X')

crc = crc16_ccitt(qris_for_crc)
qris_dynamic = qris_for_crc + crc

# Generate QR code
img = qrcode.make(qris_dynamic)
img.save("qris_" + amount + ".png")

print(f"QRIS QR code for {int(amount):,} IDR saved as qris_{amount}.png")