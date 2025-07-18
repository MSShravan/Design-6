# Time Complexity : O(N) for building the trie, O(L) for each input character
# Space Complexity : O(N) for the trie
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)  # sentence -> frequency
        self.is_end = False

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_prefix = ""
        
        # Build the trie with initial sentences and frequencies
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)
    
    def _insert(self, sentence: str, frequency: int = 1):
        """Insert a sentence into the trie with its frequency"""
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] += frequency
        node.is_end = True
    
    def _get_top_sentences(self, prefix: str) -> List[str]:
        """Get top 3 sentences with the given prefix, sorted by frequency then ASCII order"""
        if not prefix:
            return []
        
        # Navigate to the node representing the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Get all sentences with this prefix and their frequencies
        sentences_with_freq = [(sentence, freq) for sentence, freq in node.sentences.items()]
        
        # Sort by frequency (descending) then by ASCII order (ascending)
        sentences_with_freq.sort(key=lambda x: (-x[1], x[0]))
        
        # Return top 3 (or fewer if less than 3 exist)
        return [sentence for sentence, _ in sentences_with_freq[:3]]

    def input(self, c: str) -> List[str]:
        if c == '#':
            # End of sentence, store it and reset current prefix
            if self.current_prefix:
                self._insert(self.current_prefix, 1)
            self.current_prefix = ""
            return []
        
        # Add character to current prefix
        self.current_prefix += c
        
        # Return top 3 sentences with current prefix
        return self._get_top_sentences(self.current_prefix)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)