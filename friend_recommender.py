#!/usr/bin/env python3

class SocialNetwork:

    def __init__(self):
        #Constructor; initialize an empty social network
        self.users = {}

    def list_users(self):
        #List all users in the network
        #Returns: [str]: A list of usernames
        return self.users.keys()

    def add_user(self, user):
        #Add a user to the network
        #This user will have no friends initially.
        #Arguments: user (str): The username of the new user
        #Returns: None
        self.users[user] = []

    def add_friend(self, user, friend):
        #adds a friend to a user
        #"friends" go one way = following someone
        #if friend or user is not in the network, add them to the network
        ''' Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed
        Returns:
            None'''
        self.users[user].append(friend)

    def get_friends(self, user):
        ''' Get the friends of a user
        Arguments:
            user (str): The username of the user whose friends to return
        Returns:
            [str]: The list of usernames of the user's friends
        '''
        friends = self.users[user]
        return friends

    #def jaccard_index(self, user_1, user_2):
        #set_user1 = set(self.users[user_1])
        #set_user2 = set(self.users[user_2])
        #common_friends = set_user1.intersection(set_user2)
        #total_friends = set_user1.union(set_user2)
        #jacc = common_friends / total_friends
        #return jacc


        #the number of things in common / the total number of things
        #___________________________________________________________
        # find the amount of users in common
        #common_friends = 0
        #i = 0
        #while i < len(self.users.get(user_1)):
        #    j = 0
        #    while j <len(self.users.get(user_2)):
        #        if self.users.get(user_1)[i] == self.users.get(user_2)[j]:
        #            common_friends += 1
        #        j += 1
        #    i += 1
        #finding the total number of things/friends
        #total_friends = len(self.users.get(user_1)) + len(self.users.get(user_2)) - common_friends
        #jacc = common_friends / total_friends
        #return jacc




        #c = 0
        #i = 0
        #if i < len(self.users.get(user_1)):
        #    j = 0
        #    if j < len(self.users.get(user_2)):
        #        if self.users.get(user_1)[i] == self.users.get(user_2)[j]:
        #            c += 1
        #        j += 1
        #    i += 1
        # find the amount of friends
        #friends = len(self.users.get(user_1)) + len(self.users.get(user_2)) - c
        # divide common by friends
        #result = c / friends

        #return result

    def followers(self, user):
        # initialize number
        n = 0
        # write for loop that sees if user is following and adds one to number
        # alexis hates for loops
        # hil thinks for loop is the best choice for this function
        # alexis is ok with that but hil should probably write this part
        # hil agrees
        # robby: stop talking in the third person everybody
        # alexis says shut up
        # hil is wondering why her wifi is SO BAD
        for k in self.users:
            for v in self.users[k]:
                if user in v:
                    n += 1
        # return number of followers
        return n

    def suggest_friend(self, user):
        values = list(self.users.values()) #values = usernames of the people they're following
        keys = list(self.users.keys()) #keys = each user in the social network
        user_friends = self.users[user] #the list of users the primary user is following (values)
        set_friends = set(user_friends)
        highest_jacc = 0
        username = str(user)
        most_common_friends_list = []

        #comparing the primary user to all the other users
        i = 0
        while i < len(self.list_users()): #making sure the loop isn't longer than the entire network
            compared_user = set(values[i])
            common_friends = len(set_friends.intersection(compared_user))
            total_friends = len(set_friends.union(compared_user))
            if total_friends == 0: #can't divide by 0, that'll f*** it up
                return None
            else:
                #here comes the jaccard index calculation
                jaccard_index = common_friends / total_friends
                # making sure the answer isn't the user we're looking at
                if not str(keys[i]) == username:
                    #since highest_jacc starts at 0, this will happen 1st time fo'sho
                    #storing the highest jaccard index as we go along
                    if jaccard_index > highest_jacc:
                        highest_jacc = jaccard_index
                        most_common_friends = values[i] #ehhhh
            i += 1

        #making sure the answer isn't the user AKA jesse -> jesse
            #the most similar user is the user itself, but that's not helpful...
        if username in most_common_friends_list:
            most_common_friends.remove(username)

        for h in range(len(most_common_friends_list)):
            if not h in user_friends:
                if not most_common_friends[h] == username:
                    most_common_friends_list.append(most_common_friends)

        #removing people who they're already friends with
        removing_friends = set(most_common_friends_list) - set_friends
        if len(list(removing_friends)) == 0:
            return None
        #no friends to suggest

        a = 0
        most_friends = 0
        new_bff = ""
        values = self.users.values()  # values = usernames of the people they're following
        while a < len(list(removing_friends)):
            amount_friends = 0
            for bleh in values:
                if amount_friends > most_friends:
                    amount_friends = most_friends
                    new_bff = str(list(removing_friends[a]))
                if list(removing_friends[a]) in bleh:
                    most_friends += 1
            a += 1
        return new_bff

        #while i < len(values):
        #    values(i)
        #set_user1 = set(self.users[user_1])
        #set_user2 = set(self.users[user_2])
        #common_friends = set_user1.intersection(set_user2)
        #total_friends = set_user1.union(set_user2)
        #jacc = common_friends / total_friends


        # initialize
        #p = " "
        #s = user
        #max = 0
        # create for loop that tests the jaccard index of each other user and finds the highest one
        # so many for loops why
        # shut up
        #for person in self.list_users():
        #    if person != s:
        #        x = self.jaccard_index(s, person)
        #        if x > max:
        #            max = x
        #            p = person
        #max2 = 0
        #best = ""
        # create for loop that finds the best choice to recommend
        # noooo
        #for friend in self.users[p]:
        #    if friend not in self.users[user]:
        #        if self.followers(friend) > max2:
        #            max2 = self.followers(friend)
        #            best = friend
        #        return best
            #else:
             #   return None


    # don't touch this one Alexis
    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file
    Arguments:
        filename (str): The name of the network file
    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network

def main():
    network = create_network_from_file('simple.network')
    print(network.to_dot())
    print(network.suggest_friend('bailey'))

if __name__ == '__main__':
    main()
