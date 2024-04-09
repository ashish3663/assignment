class DataStream:
    def __init__(self):
        self.last_printed = {}  

    def should_output_data_str(self, timestamp, data_string):
        last_timestamp = self.last_printed.get(data_string, -5)
        print("last_timestamp--",last_timestamp)
        print("timestamp before condition---",timestamp)
        if timestamp - last_timestamp >= 5:
            print("timestamp--------",timestamp)
            self.last_printed[data_string] = timestamp
            print("last_printed----",self.last_printed)
            return True
        else:
            print("timestamp in false value===",timestamp)
		
            return False

# Usage example
data_stream = DataStream()
output = [
    data_stream.should_output_data_str(timestamp=0, data_string="hello"),
    data_stream.should_output_data_str(timestamp=1, data_string="world"),
    data_stream.should_output_data_str(timestamp=6, data_string="hello"),
    data_stream.should_output_data_str(timestamp=7, data_string="hello"),
    data_stream.should_output_data_str(timestamp=8, data_string="world")
]
print(output)