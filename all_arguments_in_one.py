def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, i hope you are having a great {time_of_day}")

  if kwargs:
    print('your taks for the day are:')
    for key, val in kwargs.items():
      print(f"{key} => {val}")

greeting('morning',
         'spencer', 'van patten',
         first = 'empty dishwasher',
         second = 'take dog outside',
         third = 'math homework')