import integrations.svd_caller as svd_caller
import integrations.nike_caller as nike_caller
import integrations.sns_caller as sns_caller

nike = nike_caller.getSneakers()
svd = svd_caller.getSneakers()
sns = sns_caller.getSneakers()

#TODO:
    # - Missing the browser location on SNS
    # - Missing END. integration
    # - Also maybe New Balance
    # - Turn this into a discord bot, that will send the info to the chat
    # - Should propably scan each hour and check if the notification of the specific shoe was sent before

nike.extend(svd)
nike.extend(sns);

for sneaker in nike:
    print(sneaker)