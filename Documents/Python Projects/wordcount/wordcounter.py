programrunning= True
while programrunning:
    usersentence = input("\nPlease enter a sentence or a paragraph (just press Enter to exit):  \n")
    cleanedsentence = usersentence.strip()

    if cleanedsentence == "":
      print("\nExiting the Word Counter. Goodbye!\n")
      programrunning=False
      continue
    words = cleanedsentence.split()
    wordcount=len(words)

    print(f"Your sentence has {wordcount} words.")