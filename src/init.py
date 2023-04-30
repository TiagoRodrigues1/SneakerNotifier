import integrations.svd_caller as svd_caller
import integrations.nike_caller as nike_caller
import integrations.sns_caller as sns_caller
import integrations.end_caller as end_caller

#svd = svd_caller.getSneakers()
nike = nike_caller.getSneakers()
end = end_caller.getSneakers()
sns = sns_caller.getSneakers()

#TODO:
    # - Missing the browser location on SNS
    # - Also maybe New Balance
    # - Turn this into a discord bot, that will send the info to the chat
    # - Should propably scan each hour and check if the notification of the specific shoe was sent before

nike.extend(end)
nike.extend(sns)

for sneaker in nike:
    print(sneaker)