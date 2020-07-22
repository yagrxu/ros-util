import argparse, os, json

command = []
command.append('aliyun')
command.append('ros')
parser = argparse.ArgumentParser()
parser.add_argument('api', help='api for running "aliyun ros"')
parser.add_argument('-f', '--file', required=True, help='parameter file')

args = parser.parse_args()
data = None
api_data = None
# aliyun ros CreateStack --StackName fcDemo --RegionId eu-central-1 --TemplateBody '$(cat ./fc/service.json)' --Parameters.1.ParameterKey  'Description' --Parameters.1.ParameterValue 'test stack' --Parameters.2.ParameterKey 'InternetAccess' --Parameters.2.ParameterValue 'false' --Parameters.3.ParameterKey 'ServiceName' --Parameters.3.ParameterValue 'fcDemo'
# aliyun ros DeleteStack --StackId $(aliyun ros ListStacks --RegionId eu-central-1 --StackName.1 fcDemo | jq '.Stacks[0].StackId' -r)
if args.file:
  with open(args.file, 'r') as parameters_file:
    data = json.load(parameters_file)
    
    

if args.api:
  command.append(args.api)
  if args.api == 'CreateStack':
    command.append('--StackName')
    command.append(data['name'])
    command.append('--RegionId')
    command.append(data['region'])
    api_data = data[args.api]
    command.append('--TemplateBody')
    command.append('"$(cat {})"'.format(os.path.join(os.path.dirname(args.file), api_data['fileUrl'])))
    index = 1
    for key, value in api_data['parameters'].items():
      command.append("--Parameters.{}.ParameterKey".format(index))
      command.append(key)
      command.append("--Parameters.{}.ParameterValue".format(index))
      command.append(value)
      index += 1
  elif args.api == 'DeleteStack':
    command.append('--StackId')
    command.append("$(aliyun ros ListStacks --RegionId {0} --StackName.1 {1} | jq '.Stacks[0].StackId' -r)".format(data['region'], data['name']))
  else:
    pass

os.system(' '.join(command))

def validate_parameter():
  pass