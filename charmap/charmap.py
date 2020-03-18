class CharMap:
    def __init__(self, init_str: str):
        self.init_str = init_str
        self.mapping = {}

    def create_mapping(self, check_str: str) -> bool:
        if len(self.init_str) < len(check_str):
            return False

        for idx in range(len(self.init_str)):
            key = self.init_str[idx]
            value = self.__get_char_at_idx(check_str, idx)
            try:
                self.put(key, value)
            except ValueError:
                return False
        return True

    def put(self, key: str, value: str):
        if key not in self.mapping:
            self.mapping[key] = value
        else:
            if self.mapping[key] != value:
                raise ValueError(
                    "Key [{key}] already mapped to [{old_value}], attempting to map again with [{new_value}]".format(
                        key=key, old_value=self.mapping[key], new_value=value
                    )
                )

    def __get_char_at_idx(self, str_val: str, idx: int) -> str:
        return str_val[idx] if idx < len(str_val) else None
