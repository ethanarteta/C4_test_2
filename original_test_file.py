import random

# Set the player's starting stats
player_name = "Player"
player_max_hp = 100
player_current_hp = 100
player_attack = 10
player_defense = 5
player_heal = 15

# Set the enemy's starting stats
enemy_name = "Enemy"
enemy_max_hp = 50
enemy_current_hp = 50
enemy_attack = 5
enemy_defense = 3
enemy_heal = 10

# Create a list of available actions
actions = ["Attack", "Defend", "Heal"]

# Main game loop
while True:
  # Print the player's stats
  print(f"{player_name}: HP {player_current_hp}/{player_max_hp}  Attack: {player_attack}  Defense: {player_defense}  Heal: {player_heal}")
  
  # Print the enemy's stats
  print(f"{enemy_name}: HP {enemy_current_hp}/{enemy_max_hp}  Attack: {enemy_attack}  Defense: {enemy_defense}")
  
  # Print the available actions
  print("Actions:")
  for i, action in enumerate(actions):
    print(f"{i + 1}. {action}")
  
  # Get the player's action
  action = input("Enter the number of the action you want to take: ")
  action = int(action) - 1
  action = actions[action]
  
  # If the player chooses to attack
  if action == "Attack":
    # Calculate the damage dealt
  damage = player_attack - enemy_defense
  if damage < 0:
    damage = 0
  # Inflict the damage on the enemy
  enemy_current_hp -= damage
  print(f"{player_name} dealt {damage} damage to {enemy_name}!")
 # Calculate the damage dealt
    damage = player_attack - enemy_defense
    if damage < 0:
      damage = 0
    # Inflict the damage on the enemy
    enemy_current_hp -= damage
    print(f"{player_name} dealt {damage} damage to {enemy_name}!")
    
    # Check if the enemy is defeated
    if enemy_current_hp <= 0:
      print(f"{enemy_name} has been defeated!")
      break
      
  # If the player chooses to defend
  elif action == "Defend":
    # Increase the player's defense for the next round
    player_defense += 2
    print(f"{player_name} defends and increases their defense by 2!")
    
  # If the player chooses to heal
  elif action == "Heal":
    # Heal the player
    player_current_hp += player_heal
    # Make sure the player's health doesn't exceed their maximum health
    if player_current_hp > player_max_hp:
      player_current_hp = player_max_hp
    print(f"{player_name} heals for {player_heal} HP!")
    
  # The enemy's turn
  # Choose a random action for the enemy
  enemy_action = random.choice(actions)
  # If the enemy chooses to attack
  if enemy_action == "Attack":
    # Calculate the damage dealt
    damage = enemy_attack - player_defense
    if damage < 0:
      damage = 0
    # Inflict the damage on the player
    player_current_hp -= damage
    print(f"{enemy_name} dealt {damage} damage to {player_name}!")
    
    # Check if the player is defeated
    if player_current_hp <= 0:
      print(f"{player_name} has been defeated!")
      break
      
  # If the enemy chooses to defend
  elif enemy_action == "Defend":
    # Increase the enemy's defense for the next round
    enemy_defense += 2
    print(f"{enemy_name} defends and increases their defense by 2!")
    
  # If the enemy chooses to heal
  elif enemy_action == "Heal":
    # Heal the enemy
    enemy_current_hp += enemy_heal
    # Make sure the enemy's health doesn't exceed their maximum health
    if enemy_current_hp > enemy_max_hp:
      enemy_current_hp = enemy_max_hp
    print(f"{enemy_name} heals for {enemy_heal} HP!")

# Game over
print("Game over!")
print("Sorry!")
