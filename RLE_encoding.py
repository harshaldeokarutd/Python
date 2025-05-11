class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Where to write in the array
        read = 0   # Where to read in the array

        while read < len(chars):
            current_char = chars[read]
            count = 0

        # Count how many times the current character repeats
            while read < len(chars) and chars[read] == current_char:
               read += 1
               count += 1

            # Write the character
            chars[write] = current_char
            write += 1

        # If the character repeats more than once, write the count digits
            if count > 1:
                for digit in str(count):
                  chars[write] = digit
                  write += 1

        return write  # Length of the compressed list