#!/usr/bin/env python3


class SocialNetwork:

    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        self.users = {}

    def list_users(self):
        '''List all users in the network

        Returns:
            [str]: A list of usernames
        '''
        #users = []
        #for friend in self:
         #   if friend not in users:
          #      users.append(friend)
        #return users.join(str(x) for x in users)
        return self.users.keys()

    def add_user(self, user):
        '''Add a user to the network

        This user will have no friends initially.

        Arguments:
            user (str): The username of the new user

        Returns:
            None
        '''
        self.users[user] = []


    def add_friend(self, user, friend):
        '''Adds a friend to a user

        Note that "friends" are one-directional - this is the equivalent of
        "following" someone.

        If either the user or the friend is not a user in the network, they
        should be added to the network.

        Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed

        Returns:
            None
        '''
        self.users[user].append(friend)


    def get_friends(self, user):
        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        friends = self.users[user]
        return friends

    def jaccard_index(self, user_1, user_2):
        # find the amount of users in common
        c = 0
        i = 0
        if i < len(self.users.get(user_1)):
            j = 0
            if j < len(self.users.get(user_2)):
                if self.users.get(user_1)[i] == self.users.get(user_2)[j]:
                    c += 1
                j += 1
            i += 1
        # find the amount of friends
        friends = len(self.users.get(user_1)) + len(self.users.get(user_2)) - c
        # divide common by friends
        result = c / friends

        return result

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
        # initialize
        p = " "
        s = user
        max = 0
        # create for loop that tests the jaccard index of each other user and finds the highest one
        # so many for loops why
        # shut up
        for person in self.list_users():
            if person != s:
                x = self.jaccard_index(s, person)
                if x > max:
                    max = x
                    p = person
        max2 = 0
        best = ""
        # create for loop that finds the best choice to recommend
        # noooo
        for friend in self.users[p]:
            if friend not in self.users[user]:
                if self.followers(friend) > max2:
                    max2 = self.followers(friend)
                    best = friend
                return best
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
    network = create_network_from_file('intermediate.network')
    print(network.to_dot())
    print(network.suggest_friend('tory'))


if __name__ == '__main__':
    main()
