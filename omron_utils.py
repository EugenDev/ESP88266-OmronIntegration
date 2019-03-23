def extract_int_value_from_hex_string(hex_string, binary_index_from, binary_index_to = None):
    hex_string_length = len(hex_string)
    as_int = int(hex_string, base=16)
    as_binary_str = bin(as_int)[2:].zfill(hex_string_length * 4)
    return int(as_binary_str[binary_index_from: binary_index_to], base=2)

def read_normal_line(port):
    return port.readline().decode("utf-8").strip()

def wait_exchange(port):
    while True:
        line = read_normal_line(port)
        print(line)
        if line == "EXH":
            return True

def wait_value_lines(port):
    while True:
        current_line = read_normal_line(port)
        if current_line[0] != 'n':
            continue
        systolic_pressure_line = read_normal_line(port)
        diastolic_pressure_line = read_normal_line(port)
        pulse_line = read_normal_line(port)
        return systolic_pressure_line, diastolic_pressure_line, pulse_line

import struct
def get_float_value_from_hex(hex_string):
    return struct.unpack('!f', bytes.fromhex(hex_string))

def get_measure_results(port):
    wait_exchange(port)
    lines = wait_value_lines(port)
    systolic_pressure = extract_int_value_from_hex_string(lines[0][1:], 1, 9)
    diastolic_pressure = extract_int_value_from_hex_string(lines[1][1:], 1, 9)
    pulse = extract_int_value_from_hex_string(lines[2][1:], 0)
    return systolic_pressure, diastolic_pressure, pulse