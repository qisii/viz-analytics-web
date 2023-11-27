from django.shortcuts import render, redirect

# added
import json
from django.http import HttpResponse
import pandas as pd
import numpy as np
from .models import Dengue
from io import BytesIO, StringIO
import base64
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import io
import datetime

# Create your views here.

# do not send an HTML page
# send back data in a form of JSON


def index(request):
    return render(request, 'visualize/index.html')

def home(request):
    return render(request, 'visualize/index.html')

# YEARLY TRENDS OF CASES AND DEATHS
# def project1(request):
#     # Load data from the Dengue model
#     dengue_data = Dengue.objects.all()

#     # Create a DataFrame from the Django QuerySet
#     df = pd.DataFrame(list(dengue_data.values()))

#     # Drop rows with empty 'loc'
#     df = df.dropna(subset=['loc'])

#     # Replace empty values in 'cases' and 'deaths' with 0
#     df['cases'] = df['cases'].fillna(0)
#     df['deaths'] = df['deaths'].fillna(0)

#     # Convert 'date' column to pandas datetime type and remove the time component
#     df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

#     # Create a new 'year' column by extracting the year from the 'date' column
#     df['year'] = pd.to_datetime(df['date'], errors='coerce').dt.year

#     # Capture unique locations of the 'loc' column
#     locations = df['loc'].unique()

#     # Compute overall stats
#     overall_stats = df.groupby('year').agg({'cases': 'sum', 'deaths': 'sum'}).reset_index()

#     # Plot graph
#     plt.figure(figsize=(9, 5))
#     plt.plot(overall_stats['year'], overall_stats['cases'], label='Cases')
#     plt.plot(overall_stats['year'], overall_stats['deaths'], label='Deaths')
#     plt.xlabel('Year')
#     plt.ylabel('Count')
#     plt.title('Dengue Cases and Deaths Over the Years')
#     plt.legend()
#     plt.grid(True)
#     plt.tight_layout()

#     # Save the plot to an image
#     img_buf = io.BytesIO()
#     plt.savefig(img_buf, format='png')
#     img_buf.seek(0)
#     img_data = base64.b64encode(img_buf.read()).decode('utf-8')

#     # narration
#     narration = "The graph illustrates yearly trends of Dengue cases and deaths over the years."
    
#     # Pass data to the template
#     context = {
#         'dengue_data': df.head(5).to_dict(orient='records'),
#         'graph_image': f'data:image/png;base64,{img_data}',
#         'narration': narration,
#     }

#     return render(request, 'visualize/project1.html', context)

def project1(request):
    # Load data from the Dengue model
    dengue_data = Dengue.objects.all()

    # Create a DataFrame from the Django QuerySet
    df = pd.DataFrame(list(dengue_data.values()))

    # Drop rows with empty 'loc'
    df = df.dropna(subset=['loc'])

    # Replace 'SISQUIJOR' with 'SIQUIJOR' in the 'loc' column
    df['loc'] = df['loc'].replace('SISQUIJOR', 'SIQUIJOR')

    # Replace empty values in 'cases' and 'deaths' with 0
    df['cases'] = df['cases'].fillna(0)
    df['deaths'] = df['deaths'].fillna(0)

    # Convert 'date' column to pandas datetime type and remove the time component
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

    # Create a new 'year' column by extracting the year from the 'date' column
    df['year'] = pd.to_datetime(df['date'], errors='coerce').dt.year

    # Create a new 'year' column by extracting the year from the 'date' column
    df['month'] = pd.to_datetime(df['date'], errors='coerce').dt.month

    # Capture unique locations of the 'loc' column
    # locations = df['loc'].unique()
    locations = sorted(df['loc'].unique())

    # Capture unique years and months for dropdown options
    unique_years = sorted(df['year'].unique())
    # unique_months = sorted(df['date'].apply(lambda x: x.strftime('%B')).unique())
    unique_months = sorted(df['date'].apply(lambda x: x.strftime('%B')).unique(), key=lambda x: datetime.datetime.strptime(x, '%B'))

    print(df.head(5))
    # narration
    narration = "The graph illustrates yearly trends of Dengue cases and deaths over the years."

    # Handle user input
    if request.method == 'POST':
        selected_year = request.POST.get('year')
        selected_month = request.POST.get('month')
        selected_location = request.POST.get('location')

        # Perform data filtering based on user input
        if selected_year:
            df = df[df['year'] == int(selected_year)]
        if selected_month:
            df = df[df['date'].apply(lambda x: x.strftime('%B')) == selected_month]
        if selected_location:
            df = df[df['loc'] == selected_location]

        # Recalculate overall stats
        overall_stats = df.groupby('year').agg({'cases': 'sum', 'deaths': 'sum'}).reset_index()

        # Print the overall sum of cases and deaths each year
        print("Overall Sum of Cases and Deaths Each Year:")
        print(overall_stats)

        # Plot graph
        plt.figure(figsize=(9, 5))
        plt.plot(overall_stats['year'], overall_stats['cases'], label='Cases', marker='o')
        plt.plot(overall_stats['year'], overall_stats['deaths'], label='Deaths', marker='o')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title('Dengue Cases and Deaths Over the Years')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save the plot to an image
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        # used to convert the binary image data into base64-encoded string.
        # this is to embed the image directly into HTML or other text-based formats.
        img_data = base64.b64encode(img_buf.read()).decode('utf-8')

    else:
        # By default, show overall stats if the input fields are empty
        overall_stats = df.groupby('year').agg({'cases': 'sum', 'deaths': 'sum'}).reset_index()

        # Print the overall sum of cases and deaths each year
        print("Overall Sum of Cases and Deaths Each Year:")
        print(overall_stats)

        # Plot graph
        plt.figure(figsize=(9, 5))
        plt.plot(overall_stats['year'], overall_stats['cases'], label='Cases', marker='o')
        plt.plot(overall_stats['year'], overall_stats['deaths'], label='Deaths', marker='o')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title('Dengue Cases and Deaths Over the Years')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save the plot to an image
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        img_data = base64.b64encode(img_buf.read()).decode('utf-8')

    # Pass data to the template
    context = {
        'dengue_data': df.head(5).to_dict(orient='records'),
        'graph_image': f'data:image/png;base64,{img_data}',
        'narration': narration,
        'unique_years': unique_years,
        'unique_months': unique_months,
        'locations': locations,
    }

    return render(request, 'visualize/project1.html', context)


# Mapping
def project2(request):
    return render(request, 'visualize/project2.html')


# Bonus
def project3(request):
    return render(request, 'visualize/project3.html')
