from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
	    "my_list": [
	    #restaurant 1
	    
		    {
		    "restaurant_name": "fay",
		    "food_type" : "japanese"
		    },
		    #restaurant 2
		    {
		    "restaurant_name": "aisha",
		    "food_type" : "italian"
		    },
		    #restaurant 3
		   {
		    "restaurant_name": "laila",
		    "food_type" : "vegan"
		    }

	    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
    		"restaurant_name" : "sinless",
    		"food_type" : "healthy"
    	}

    }
    return render(request, 'detail.html', context)
