from django.shortcuts import render

def policy(request):
    return render(request, 'policy.html')



def calculate_premiums(self):
        '''Calculate the quick quote premiums for each limit and deductible'''
        self.premiums = []
        for limit in self.fields['state_limit'].queryset:
            for deduct in self.fields['deductible'].queryset:
                dedlim = DedLimitPremium(
                    limit=limit,
                    deductible=deduct,
                    premium=deduct.value + 100
                )
                self.premiums.append(dedlim)
        self.fields['expiring_premium'].widget.attrs.update(
            {'autofocus': ''}
        )