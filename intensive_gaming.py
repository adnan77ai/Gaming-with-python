player1_score = 0
player2_score = 0

while True :
  player_1 = input ("Player_1> :")
  player_2 = input ("Player_2> :")
  
  if player_1 == 'R' :
    if player_2 == 'R' :
      print ("Each player applies the same move, Draw!")
    elif player_2 == 'P' :
      print ("Player 2 wins the round!")
      player2_score += 1
    elif player_2 == 'S' :
      print ("player 1 wins the round!")
      player1_score += 1
  elif player_1 == 'S' :
    if player_2 == 'R' :
      print ("Player 2 wins the round!")
      player2_score += 1
    elif player_2 == 'P' :
      print ("player 1 wins the round!")
      player1_score += 1
    elif player_2 == 'S' :
      print ("Each player applies the same move, Draw!")
  elif player_1 == 'P' :
    if player_2 == 'R' :
      print ("player 1 wins the round!")
      player1_score += 1
    elif player_2 == 'P' :
      print ("Each player applies the same move, Draw!")
    elif player_2 == 'S' :
      print ("Player 2 wins the round!")
      player2_score += 1
  print ('Player_1 wins', player1_score, 'points')
  print ('Player_2 wins', player2_score, 'points')

  if player1_score == 3 :
    print ("Player_1 wins the game")
    break
  elif player2_score == 3 :
    print ("Player_2 wins the game")
    exit()
  else :
    continue
print ('Thanks for playing')