import json

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre+[key, '{}']
                    print( "pre+[key, '{}']:",pre+[key, '{}'])
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
                        print("d:",d)
            elif isinstance(value, list):
                if len(value) == 0:                   
                    yield         
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
                            print("d:",d)
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                    print( "pre+[key, '{}']:",pre+[key, '{}'])
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
                            print("d:",d)
            else:
                yield pre + [key, value]
                print( "pre + [key, value]:",pre + [key, value])
    else:
        yield indict

if __name__ == '__main__':
    # with open("2D.json", 'r') as file:
    #     str = file.read()
    #     data = json.loads(str)
    #     print(data)
    #     print(type(data))
    #     for item in dict_generator(data):
    #         print(item)

    a= {'header': {'timestamp': '1571636645488',
  'frameId': 'quanergy',
  'sequence': 15377},
 'object': [{'id': '4496',
   'timestamp': '1571636645488',
   'position': {'x': 14.6418629, 'y': -10.6926031, 'z': -2.01485038},
   'size': {'x': 0.519170225, 'y': 0.518952787, 'z': 0.0456985086},
   'velocity': {'x': 0.515208244, 'y': -0.343170881, 'z': -0.0737518221},
   'objectClass': 'HUMAN'},
  {'id': '4556',
   'timestamp': '1571636645488',
   'position': {'x': 15.3042717, 'y': -9.68118572, 'z': -2.01950383},
   'size': {'x': 0.66631937, 'y': 0.234836429, 'z': 0.026046142},
   'velocity': {'x': -0.0135841537, 'y': 0.0106180822, 'z': -0.00242288853},
   'objectClass': 'HUMAN'},
  {'id': '4558',
   'timestamp': '1571636645488',
   'position': {'x': 1.9795996, 'y': -6.09465933, 'z': -1.66131747},
   'size': {'x': 3.5219245, 'y': 1.74867713, 'z': 1.52694786},
   'velocity': {'x': -0.563834906, 'y': -0.00195267494, 'z': 0.169498235},
   'objectClass': 'VEHICLE'}]}

    for item in dict_generator(a):
        print(item)
        # pass