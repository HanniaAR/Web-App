import notes.note as n

class Actions:

    def create(self, user):
        print(f'\n{user[1]} vas a crear nueva nota')
        title = input('Introduce the title of your note: ')
        desc = input('Write your note: ')

        note = n.Note(user[0], title, desc)
        save = note.save()

        if note[0] >= 1:
            print(f'Note already saved: {note.title}')
        else:
            print(f'\nNote not saved, sorry {user[0]}')