from .models import Locker, LockerUser, Ownership, LockerConfirmation
from django.shortcuts import get_object_or_404, render
from .forms import RegisterExternalLockerUserForm, RegisterInternalLockerUserForm
from django.http import Http404

def view_lockers(request):
    lockers = Locker.objects.all()
    context = {
        "lockers":lockers,
    }
    return render(request, 'lockers/list.html', context)



def register_locker_external(request, number):
    # Fetch requested locker
    locker = Locker.objects.get(number=number)
    if not locker.is_free():
        # Locker was already taken
        raise Http404

    form = RegisterExternalLockerUserForm(request.POST or None)
    if form.is_valid():
        # Check if user already exists
        instance = form.save(commit=False)
        user = LockerUser.objects.filter(username=instance.username)[0]
        if not user:
            # User not found. Create user
            instance.save()
            user = instance

        if user.reached_limit():
            # User has reached the active locker limit
            raise Http404

        # Create a new ownership for the user
        new_ownership = Ownership.objects.add(locker=locker, user=user)
        user.ownerships.add(new_ownership)
        confirmation_object = LockerConfirmation.objects.create(ownership=new_ownership)
        confirmation_object.save()

        context  = {
            "confirmation": confirmation_object,
            "user": user,
            "ownership": new_ownership,
        }

    context = {
        "form": form,
    }
    return render(request, 'lockers/register2.html', context)


def register_locker_internal(request, number):
    pass


def register_locker(request, number):
    if Locker.objects.get(number=number).is_free():
        if request.user.is_authenticated():
            register_locker_external(request, number)
        else:
            # Internal
            register_locker_external(request, number)
    else:
        raise Http404



    context = {
        "number": number,
    }

    if request.user.is_authenticated():
        if request.POST == True:
            # If the logged in user has confirmed locker
            locker = Locker.objects.get(pk=number)
            if not locker.is_free():
                locker_user = LockerUser.objects.get(internal_user=request.user)
                if locker_user:
                    pass
                    # Count this locker users' lockers and check that its lower than the limit
                else:
                    pass
                    # Create locker_user
                # Send mail
            else:
                pass
                # This is awkward. The locker is already in user
        else:
            pass
            # User has not clicked yes
            # Give a confirmation of sorts ?
            # This can probably be moved to a modal/popup during locker selection
    else:
        pass
        # User is not internal user
        form = RegisterExternalLockerUserForm
        # Very simiilar logic to the one above
    return render(request, 'lockers/register.html', context)

