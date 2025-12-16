from abc import ABC, abstractmethod

class DataTransformer(ABC):

    @abstractmethod
    def transform(self, source_data):
        pass


class CsvToJsonTransformer(DataTransformer):

    def transform(self, csv_data) -> str:
        print("-> Performing CSV to JSON transformation.")
        json_output = (f'{{"source": "csv", "data": "'
                       f'{csv_data.replace(",", "; ")}", "status": "transformed"}}')
        return json_output


class IostreamToJsonTransformer(DataTransformer):

    def transform(self, stream_data) -> str:
        # In a real scenario, this would contain the logic to read
        # from the stream and convert it to a JSON string.
        print("-> Performing I/O Stream to JSON transformation.")
        json_output = (f'{{"source": "iostream", "data": '
                       f'"{stream_data.strip()}", "status": "transformed"}}')
        return json_output



    transformer = CsvToJsonTransformer()
    transformed_json = transformer.transform("1,2,3")


