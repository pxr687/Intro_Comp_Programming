from jupyprint import jupyprint

def check_final_ans(reader_interest, newspaper):
    # For the first conditional statements exercise, last question.
    if reader_interest == 'General News':
        assert newspaper == 'Thai Rath', "Hmm, it looks like you didn't do that right. Your newspaper does not match the reader interest!"
    elif reader_interest == 'Business':
        assert newspaper == 'Bangkok Post', "Hmm, it looks like you didn't do that right. Your newspaper does not match the reader interest!"
    elif reader_interest == 'Politics':
        assert newspaper == 'Matichon', "Hmm, it looks like you didn't do that right. Your newspaper does not match the reader interest!"
    elif reader_interest == 'Entertainment':
        assert newspaper == 'Daily News', "Hmm, it looks like you didn't do that right. Your newspaper does not match the reader interest!"
    else:
        assert newspaper == 'Online News / Other', "Hmm, it looks like you didn't do that right. Your newspaper does not match the reader interest!"

    jupyprint('You passed this question! Well done!')