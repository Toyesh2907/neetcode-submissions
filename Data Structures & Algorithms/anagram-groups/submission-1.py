def create_frequence_map(string: str, index: int) -> dict:
    # frequence_map = {"string_index": index}
    frequence_map = {}
    for character in string:
        try:
            frequence_map[character] += 1
        except KeyError:
            frequence_map[character] = 1
            
    return frequence_map

def group_equal_frequence_strings(
    string_list: List[str], 
    frequence_map_list: List[dict]
) -> List[List[str]]:

    grouped_anagrams:List[List[str]] = []
    added_elements_index = []
    for index in range(len(frequence_map_list)):
        if index not in added_elements_index:
            added_elements_index.append(index)
            current_group = []
            current_group.append(string_list[index])
            for index_plus in range(index + 1, len(frequence_map_list)):
                    if frequence_map_list[index] == frequence_map_list[index_plus]:
                        added_elements_index.append(index_plus)
                        current_group.append(string_list[index_plus])
            grouped_anagrams.append(current_group)
    return grouped_anagrams

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]] :
        if len(strs) == 1:
            return [strs]

        frequence_map_list = [] 
        for index, string in enumerate(strs):
            frequence_map_list.append(create_frequence_map(string = string, index = index))

        
        grouped_anagrams = group_equal_frequence_strings(strs, frequence_map_list) 
        print(grouped_anagrams)
        return grouped_anagrams