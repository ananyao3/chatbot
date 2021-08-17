number = 0
print ("Welcome to Makeup.ca!")
name = input ("What is your name?")
print (" ")
print ("Hi", name, "! My name is Ananya and I will be your virtual makeup assistant.")
while number == 0:
    print (" ")
    question = input ("What can I help you with today? Foundation or lip products?")
    if question == 'foundation':
        number = 1
        while number == 1:
            print (" ")
            question = input ("What type of foundation are you looking for? Liquid, powder or tinted moisturizer? Or, are you unsure?")
            if question == 'liquid':
                number = 2
                print (" ")
                print ("For context, liquid foundation is often used to provide the most coverage and is best used to even out large patches of skin. Depending on your skin type, there are various liquid foundations that can be used to give you the best finish.")
                while number == 2:
                    print (" ")
                    question = input ("Do you have oily or dry skin?")
                    if question == 'oily' or question == 'oily skin':
                        number = 3
                        print (" ")
                        print ("Since oily skin tends to break up the ingredients in liquid foundation throughout the day, it can look patchy after wearing it for a long time. Hence, I recommend purchasing a liquid foundation that mattifies your skin and keeps it from getting oily as quick.")
                        print (" ")
                        print ("If you are looking for a drugstore option, the L'Oréal Paris Infallible Pro-Matte Foundation is good! It is $11 CAD, is a longwear foundation and has 22 shades to choose from.")
                        print (" ")
                        print ("For a mid-priced foundation, the Fenty Beauty Pro Filt'r Soft Matte Longwear Foundation is the way to go! It is $47 CAD, is longlasting and has 50 shades to choose from!")
                        print (" ")
                        print ("Finally, for the high end foundation, Clé de Peau Beauté's Radiant Fluid Foundation Matte Broad Spectrum SPF 20 Sunscreen is great! Although it is $170 CAD, it has 24 shades and SPF 20 built into it to protect your skin from UV rays!")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes, first' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'one' or question == 'Loreal' or question == 'first' or question == '$11 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Loreal Paris' or question == 'Loreal Paris Infalliable Pro-Matte Foundation':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the L'Oréal Paris Infallible Pro-Matte Foundation: https://www.walmart.ca/en/ip/loral-paris-pro-matte-foundation-oil-free-lightweight-longwear-face-makeup-up-to-24hr-classic-ivory-30-ml-buff/6000189234930")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty foundation' or question == 'Fenty Beauty' or question == 'Fenty Beauty Pro Filtr Soft Matte Longwear Foundation' or question == 'Fenty':
                                print (" ")
                                print ("Here is the website to purchase the Fenty Beauty Pro Filt'r Soft Matte Longwear Foundation: https://www.sephora.com/ca/en/product/pro-filtr-soft-matte-longwear-foundation-P87985432?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-AF1e7Eu.gUFiS2tdtaKJRA&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-AF1e7Eu.gUFiS2tdtaKJRA&ranLinkID=10-1&browserdefault=true")
                                number = 4
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes third' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Cle' or question == 'Cle de Peau Beaute' or question == 'Radiant Fluid Foundation':
                                print (" ")
                                print ("Here is the website to purchase the Clé de Peau Beauté Radiant Fluid Foundation Matte Broad Spectrum SPF 20 Sunscreen: https://www.saksfifthavenue.com/product/cl%C3%A9-de-peau-beaut%C3%A9-radiant-fluid-foundation-matte-broad-spectrum-spf-20-sunscreen-0400012969542.html?ranMID=13816&ranEAID=tv2R4u9rImY&ranSiteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&site_refer=AFF001&mid=13816&siteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&LSoid=894953&LSlinkid=10&LScreativeid=1")
                                number = 4
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")   
                    elif question == 'dry' or question == 'dry skin':
                        number = 3
                        print (" ")
                        print ("To help hydrate dry skin and prevent the foundation from becoming flaky throughout the day, I recommend purchasing a hydrating liquid foundation.")
                        print (" ")
                        print ("If you are looking for a drugstore option, the Maybelline Fit Me Dewy and Smooth Foundation is good! It is $8 USD, has 24 shades and built in SPF 18.")
                        print (" ")
                        print ("For a mid-priced foundation, the Make Up For Ever Ultra HD Invisible Cover Foundation is the way to go! It is $55 CAD, hydrating, and has 50 shades!")
                        print (" ")
                        print ("Finally, for the high end foundation, the LANCÔME Le Teint Particulier Custom-Made Foundation is great! Although it is $88 CAD, it has over 72,000 shade possibilities.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == '$8 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Fit Me Dewy and Smooth Foundation' or question == 'Fit Me Dewy and Smooth Foundation' or question == 'Maybelline Fit Me Dewy':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Maybelline Fit Me Dewy and Smooth Foundation: https://www.ulta.com/p/fit-me-dewy-smooth-foundation-xlsImpprod2980151")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Make Up For Ever foundation' or question == 'Make Up For Ever' or question == 'Make Up For Ever Ultra HD Invisible Cover Foundation' or question == 'Make Up For Ever' or question == 'Ultra HD Invisible Cover Foundation' or question == 'Ultra HD foundation':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Make Up For Ever Ultra HD Invisible Cover Foundation: https://www.sephora.com/ca/en/product/ultra-hd-invisible-cover-foundation-P398321?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-79gs3VUGxm.DkZOIPCnUNQ&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-79gs3VUGxm.DkZOIPCnUNQ&ranLinkID=10-1&browserdefault=true")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Lancome foundation' or question == 'Lancome' or question == 'Lancome Le Teint Particulier Custom Made Foundation':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the LANCÔME Le Teint Particulier Custom-Made Foundation: https://www.saksfifthavenue.com/product/cl%C3%A9-de-peau-beaut%C3%A9-radiant-fluid-foundation-matte-broad-spectrum-spf-20-sunscreen-0400012969542.html?ranMID=13816&ranEAID=tv2R4u9rImY&ranSiteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&site_refer=AFF001&mid=13816&siteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&LSoid=894953&LSlinkid=10&LScreativeid=1")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                 number = 4
                                 print (" ")
                                 print ("No problem!")
                                 while number == 4:
                                     print (" ")
                                     question = input ("Would you be interested in another type of foundation instead?")
                                     if question == 'yes':
                                         number = 1
                                     elif question == 'no' or question == 'none':
                                         number = 5
                                         while number == 5:
                                             print (" ")
                                             question = input ("Would you like to keep shopping?")
                                             if question == 'yes':
                                                 number = 0
                                             elif question == 'no':
                                                 print (" ")
                                                 print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                 number = 'done'
                                             else:
                                                 print (" ")
                                                 print ("Sorry, I did not receive a valid option.")
                                     else:
                                         print (" ")
                                         print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
                                                        
            elif question == 'powder':
                number = 2
                print (" ")
                print ("For context, powder foundation is a foundation that comes in a compact and is best used for oily or combination skin as it mattifies it.")
                while number == 2:
                    print (" ")
                    question = input ("Do you have oily, dry or combination skin?")
                    if question == 'oily' or question == 'combination' or question == 'oily skin' or question == 'combination skin':
                        number = 3
                        print (" ")
                        print ("If you are looking for a drugstore option, the L'Oreal Paris True Match Loose Powder Mineral Foundation is good! It is $10 USD, comes in 11 shades and has built in SPF 19 to help protect your skin from UV rays.")
                        print (" ")
                        print ("For a mid-priced option, the KVD Beauty Lock-It Powder Foundation is great! It is $50 CAD, has 24 shades and is full coverage.")
                        print (" ")
                        print ("For a high end option, the GUCCI Poudre De Beauté Mat Naturel Face Powder is the way to go. It is $81 CAD, has 17 shades and is buildable coverage.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'first' or question == 'Loreal' or question == 'Loreal Paris True Match Loose Powder Mineral Foundation' or question == 'yes, 1' or question == 'yes 1' or question == 'yes, first' or question == 'yes first' or question == 'one' or question == 'yes one' or question == 'yes, one' or question == 'drugstore option' or question == 'drugstore':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the L'Oreal Paris True Match Loose Powder Mineral Foundation: https://www.walmart.com/ip/L-Oreal-Paris-True-Match-Loose-Powder-Mineral-Foundation-Makeup-Buff-Beige-0-35-oz/10314768")
                                while number == 4:
                                        print (" ")
                                        question = input ("Would you like to keep shopping?")
                                        if question == 'yes':
                                            number = 0
                                        elif question == 'no':
                                            print (" ")
                                            print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                            number = 'done'
                                        else:
                                            print (" ")
                                            print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'kvd beauty' or question == 'KVD beauty foundation' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the KVD Beauty Lock-It Powder Foundation: https://www.sephora.com/ca/en/product/lock-it-powder-foundation-P441024?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-1hqV6P8JjJpUQug8XEfXDA&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-1hqV6P8JjJpUQug8XEfXDA&ranLinkID=10-1&browserdefault=true")
                                while number == 4:
                                        print (" ")
                                        question = input ("Would you like to keep shopping?")
                                        if question == 'yes':
                                            number = 0
                                        elif question == 'no':
                                            print (" ")
                                            print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                            number = 'done'
                                        else:
                                            print (" ")
                                            print ("Sorry, I did not receive a valid option.")
                            elif question == 'gucci foundation' or question == 'GUCCI foundation' or question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the GUCCI Poudre De Beauté Mat Naturel Face Powder: https://www.gucci.com/ca/en/pr/gifts/gifts-for-women/accessories-for-women/01-poudre-de-beaute-mat-naturel-face-powder-p-6249799PRD90001?utm_medium=organic&utm_source=google&utm_campaign=free_pla&utm_content=pla&utm_term=6249799PRD90001_OS&gclid=Cj0KCQjwub-HBhCyARIsAPctr7x7D8ITPBwo8ABcyoVJjFrO6MTCEYVzmR96Fmam9dDqz1-LYKxeBXwaAku4EALw_wcB")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'no' or question == 'none':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")  
                    elif question == 'dry' or question == 'dry skin':
                        number = 3
                        print (" ")
                        print ("Since you have dry skin, I would not recommend purchasing a powder foundation since it will further dry your skin out and flake off throughout the day. ")
                        while number == 3:
                            print (" ")
                            question = input ("Would you be interested in another type of foundation instead?")
                            if question == 'yes':
                                number = 1
                            elif question == 'no' or question == 'nope':
                                print (" ")
                                number = 2
                                print ("No problem!")
                                while number == 2:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")

                            
            elif question == 'tinted moisturizer' or question == 'tinted' or question == 'moisturizer':
                number = 2
                print (" ")
                print ("For context, tinted moisturizer is a great alternative for people who don't want to wear foundation as it is light and breathable. Depending on your skin type, you can purchase a tinted moisturizer to best suit your needs!")
                while number == 2:
                    print (" ")
                    question = input ("Do you have oily or dry skin?")
                    if question == 'oily' or question == 'oily skin':
                        number = 3
                        print (" ")
                        print ("Since oily skin tends to break up the ingredients in a tinted moisturizer throughout the day and can clog your pores, it can look patchy after wearing it for a long time. Hence, I recommend purchasing a lightweight tinted moisturizer that mattifies your skin and keeps it from getting oily as quick.")
                        print (" ")
                        print ("If you are looking for a drugstore option, the COVERGIRL Clean Matte BB Cream is good! It is $8.97 CAD, is a mattifying tinted moisturizer and has 6 shades to choose from.")
                        print (" ")
                        print ("For a mid-priced foundation, the Tarte Amazonian Clay BB Tinted Moisturizer is the way to go! It is $48 CAD, oil free, has 2 shades and built in SPF 20 to help protect your skin from UV rays!")
                        print (" ")
                        print ("Finally, for the high end foundation, the Sisley Paris Tinted Moisturizer is great! Although it is $150 CAD, it has 4 shades and is longlasting.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes, first' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'one' or question == 'Loreal' or question == 'first' or question == '$11 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Loreal Paris' or question == 'Loreal Paris Infalliable Pro-Matte Foundation':
                                number = 4
                                print ("Here is the website to purchase the COVERGIRL Clean Matte BB Cream: https://www.walmart.ca/en/ip/covergirl-clean-matte-bb-cream-light-medium-530/6000196036398")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty foundation' or question == 'Fenty Beauty' or question == 'Fenty Beauty Pro Filtr Soft Matte Longwear Foundation' or question == 'Fenty':
                                print (" ")
                                print ("Here is the website to purchase the Tarte Amazonian Clay BB tinted moisturizer: https://www.sephora.com/ca/en/product/amazonian-clay-bb-tinted-moisturizer-broad-spectrum-spf-20-sunscreen-P67617")
                                number = 4
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes third' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Cle' or question == 'Cle de Peau Beaute' or question == 'Radiant Fluid Foundation':
                                print (" ")
                                print ("Here is the website to purchase the Sisley Paris Tinted Moisturizer: https://www.nordstrom.ca/s/sisley-paris-tinted-moisturizer/3466906")
                                number = 4
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")   
                    elif question == 'dry' or question == 'dry skin':
                        number = 3
                        print (" ")
                        print ("To help hydrate dry skin and prevent the foundation from becoming flaky throughout the day, I recommend purchasing a hydrating tinted moisturizer.")
                        print (" ")
                        print ("If you are looking for a drugstore option, the Neutrogena Protect and Tint tinted moisturizer is good! It is $8.47 USD, has 5 shades and built in SPF 30.")
                        print (" ")
                        print ("For a mid-priced foundation, the Lancôme Feels Good Tinted Moisturizer Sunscreen is the way to go! It is $50 CAD, hydrating, has 15 shades and built in SPF 23 to protect your skin from UV rays!")
                        print (" ")
                        print ("Finally, for the high end foundation, the Trish McEvoy Beauty Balm Instant Solutions is great! Although it is $87 USD, it has built in SPF 35, moisturizer and has 4 shades.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == '$8 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Fit Me Dewy and Smooth Foundation' or question == 'Fit Me Dewy and Smooth Foundation' or question == 'Maybelline Fit Me Dewy':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Neutrogena Protect and Tint tinted moisturizer: https://www.walmart.com/ip/Neutrogena-Protect-Tint-Tinted-Moisturizer-SPF-30-Shade-10-1-1-fl-oz/931175653?irgwc=1&sourceid=imp_zdzST7XA8xyLTlXyX7X%3AOWMEUkBytxUnXy3nWs0&veh=aff&wmlspartner=imp_10078&clickid=zdzST7XA8xyLTlXyX7X%3AOWMEUkBytxUnXy3nWs0&sharedid=womenshealthmag.com&affiliates_ad_id=612734&campaign_id=9383")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Make Up For Ever foundation' or question == 'Make Up For Ever' or question == 'Make Up For Ever Ultra HD Invisible Cover Foundation' or question == 'Make Up For Ever' or question == 'Ultra HD Invisible Cover Foundation' or question == 'Ultra HD foundation':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Lancôme Feels Good Tinted Moisturizer Sunscreen: https://www.sephora.com/ca/en/product/skin-feels-good-skin-nourishing-foundation-P428823")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Lancome foundation' or question == 'Lancome' or question == 'Lancome Le Teint Particulier Custom Made Foundation':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Trish McEvoy Balm Instant Solutions: https://www.trishmcevoy.com/products/beauty-balm-instant-solutions-spf-35?variant=32072318844963")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
                        
            elif question == 'unsure' or question == 'need help' or question == 'help':
                number = 2
                print (" ")
                print ("No problem!")
                while number == 2:
                    print (" ")
                    question = input ("Do you have oily or dry skin?")
                    if question == 'oily' or question == 'oily skin':
                        number = 3
                        print (" ")
                        print ("For context, liquid foundation is often used to provide the most coverage and is best used to even out large patches of skin. Since oily skin tends to break up the ingredients in liquid foundation throughout the day, it can look patchy after wearing it for a long time. Hence, I recommend purchasing a liquid foundation that mattifies your skin and keeps it from getting oily as quick.")
                        print (" ")
                        print ("Similarly, powder foundation is a foundation that comes in a compact and is best used for oily or combination skin as it mattifies it.")
                        print (" ")
                        print ("Finally, tinted moisturizer is a great alternative for people who don't want to wear foundation as it is light and breathable. Since oily skin tends to break up the ingredients in a tinted moisturizer throughout the day and can clog your pores, it can look patchy after wearing it for a long time. Hence, I recommend purchasing a lightweight tinted moisturizer that mattifies your skin and keeps it from getting oily as quick.")                  
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these types of foundations?")
                            if question == '1' or question == 'one' or question == 'yes, 1' or question == 'yes, one' or question == 'yes one' or question == 'yes 1' or question == 'first' or question == 'liquid' or question == 'liquid foundation':
                                number = 4
                                print (" ")
                                print ("If you are looking for a drugstore option, the L'Oréal Paris Infallible Pro-Matte Foundation is good! It is $11 CAD, is a longwear foundation and has 22 shades to choose from.")
                                print (" ")
                                print ("For a mid-priced foundation, the Fenty Beauty Pro Filt'r Soft Matte Longwear Foundation is the way to go! It is $47 CAD, is longlasting and has 50 shades to choose from!")
                                print (" ")
                                print ("Finally, for the high end foundation, Clé de Peau Beauté's Radiant Fluid Foundation Matte Broad Spectrum SPF 20 Sunscreen is great! Although it is $170 CAD, it has 24 shades and SPF 20 built into it to protect your skin from UV rays!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes, first' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'one' or question == 'Loreal' or question == 'first' or question == '$11 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Loreal Paris' or question == 'Loreal Paris Infalliable Pro-Matte Foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the L'Oréal Paris Infallible Pro-Matte Foundation: https://www.walmart.ca/en/ip/loral-paris-pro-matte-foundation-oil-free-lightweight-longwear-face-makeup-up-to-24hr-classic-ivory-30-ml-buff/6000189234930")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty foundation' or question == 'Fenty Beauty' or question == 'Fenty Beauty Pro Filtr Soft Matte Longwear Foundation' or question == 'Fenty':
                                        print (" ")
                                        print ("Here is the website to purchase the Fenty Beauty Pro Filt'r Soft Matte Longwear Foundation: https://www.sephora.com/ca/en/product/pro-filtr-soft-matte-longwear-foundation-P87985432?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-AF1e7Eu.gUFiS2tdtaKJRA&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-AF1e7Eu.gUFiS2tdtaKJRA&ranLinkID=10-1&browserdefault=true")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes third' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Cle' or question == 'Cle de Peau Beaute' or question == 'Radiant Fluid Foundation':
                                        print (" ")
                                        print ("Here is the website to purchase the Clé de Peau Beauté Radiant Fluid Foundation Matte Broad Spectrum SPF 20 Sunscreen: https://www.saksfifthavenue.com/product/cl%C3%A9-de-peau-beaut%C3%A9-radiant-fluid-foundation-matte-broad-spectrum-spf-20-sunscreen-0400012969542.html?ranMID=13816&ranEAID=tv2R4u9rImY&ranSiteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&site_refer=AFF001&mid=13816&siteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&LSoid=894953&LSlinkid=10&LScreativeid=1")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        number = 4
                                        print (" ")
                                        print ("No problem!")
                                        while number == 4:
                                            print (" ")
                                            question = input ("Would you be interested in another type of foundation instead?")
                                            if question == 'yes':
                                                number = 1
                                            elif question == 'no' or question == 'none':
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid response.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'two' or question == 'yes 2' or question == 'yes two' or question == 'yes, 2' or question == 'yes, two' or question == 'second' or question == 'powder' or question == 'powder foundation':
                                number = 4
                                print ("If you are looking for a drugstore option, the L'Oreal Paris True Match Loose Powder Mineral Foundation is good! It is $10 USD, comes in 11 shades and has built in SPF 19 to help protect your skin from UV rays.")
                                print (" ")
                                print ("For a mid-priced option, the KVD Beauty Lock-It Powder Foundation is great! It is $50 CAD, has 24 shades and is full coverage.")
                                print (" ")
                                print ("For a high end option, the GUCCI Poudre De Beauté Mat Naturel Face Powder is the way to go. It is $81 CAD, has 17 shades and is buildable coverage.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'first' or question == 'Loreal' or question == 'Loreal Paris True Match Loose Powder Mineral Foundation' or question == 'yes, 1' or question == 'yes 1' or question == 'yes, first' or question == 'yes first' or question == 'one' or question == 'yes one' or question == 'yes, one' or question == 'drugstore option' or question == 'drugstore':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the L'Oreal Paris True Match Loose Powder Mineral Foundation: https://www.walmart.com/ip/L-Oreal-Paris-True-Match-Loose-Powder-Mineral-Foundation-Makeup-Buff-Beige-0-35-oz/10314768")
                                        while number == 5:
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'kvd beauty' or question == 'KVD beauty foundation' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the KVD Beauty Lock-It Powder Foundation: https://www.sephora.com/ca/en/product/lock-it-powder-foundation-P441024?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-1hqV6P8JjJpUQug8XEfXDA&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-1hqV6P8JjJpUQug8XEfXDA&ranLinkID=10-1&browserdefault=true")
                                        while number == 5:
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                    elif question == 'gucci foundation' or question == 'GUCCI foundation' or question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three':
                                        number = 5
                                        print ("Here is the website to purchase the GUCCI Poudre De Beauté Mat Naturel Face Powder: https://www.gucci.com/ca/en/pr/gifts/gifts-for-women/accessories-for-women/01-poudre-de-beaute-mat-naturel-face-powder-p-6249799PRD90001?utm_medium=organic&utm_source=google&utm_campaign=free_pla&utm_content=pla&utm_term=6249799PRD90001_OS&gclid=Cj0KCQjwub-HBhCyARIsAPctr7x7D8ITPBwo8ABcyoVJjFrO6MTCEYVzmR96Fmam9dDqz1-LYKxeBXwaAku4EALw_wcB")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'three' or question == 'yes 3' or question == 'yes three' or question == 'yes, 3' or question == 'yes, three' or question == 'tinted moisturizer' or question == 'tinted moisturizer foundation' or question == 'third' or question == 'yes third' or question == 'yes, third':
                                number = 4
                                print (" ")
                                print ("If you are looking for a drugstore option, the COVERGIRL Clean Matte BB Cream is good! It is $8.97 CAD, is a mattifying tinted moisturizer and has 6 shades to choose from.")
                                print (" ")
                                print ("For a mid-priced foundation, the Tarte Amazonian Clay BB Tinted Moisturizer is the way to go! It is $48 CAD, oil free, has 2 shades and built in SPF 20 to help protect your skin from UV rays!")
                                print (" ")
                                print ("Finally, for the high end foundation, the Sisley Paris Tinted Moisturizer is great! Although it is $150 CAD, it has 4 shades and is longlasting.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes, first' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'one' or question == 'Loreal' or question == 'first' or question == '$11 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Loreal Paris' or question == 'Loreal Paris Infalliable Pro-Matte Foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the COVERGIRL Clean Matte BB Cream: https://www.walmart.ca/en/ip/covergirl-clean-matte-bb-cream-light-medium-530/6000196036398")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty foundation' or question == 'Fenty Beauty' or question == 'Fenty Beauty Pro Filtr Soft Matte Longwear Foundation' or question == 'Fenty':
                                        print (" ")
                                        print ("Here is the website to purchase the Tarte Amazonian Clay BB tinted moisturizer: https://www.sephora.com/ca/en/product/amazonian-clay-bb-tinted-moisturizer-broad-spectrum-spf-20-sunscreen-P67617")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes third' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Cle' or question == 'Cle de Peau Beaute' or question == 'Radiant Fluid Foundation':
                                        print (" ")
                                        print ("Here is the website to purchase the Sisley Paris Tinted Moisturizer: https://www.nordstrom.ca/s/sisley-paris-tinted-moisturizer/3466906")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        number = 5
                                        print (" ")
                                        question = input ("No problem! Would you be interested in another type of foundation instead?")
                                        if question == 'yes':
                                            number = 1
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'no' or question == 'none':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == 'dry' or question == 'dry skin':
                        number = 3
                        print (" ")
                        print ("For context, liquid foundation is often used to provide the most coverage and is best used to even out large patches of skin. To help hydrate dry skin and prevent the foundation from becoming flaky throughout the day, I recommend purchasing a hydrating liquid foundation.")
                        print (" ")
                        print ("Moreover, powder foundation is a lightweight foundation that comes in a compact and mattifies your skin.")
                        print (" ")
                        print ("Finally, tinted moisturizer is a great alternative for people who don't want to wear foundation as it is light and breathable. To help hydrate dry skin and prevent the foundation from becoming flaky throughout the day, I recommend purchasing a hydrating tinted moisturizer.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these types of foundations?")
                            if question == '1' or question == 'one' or question == 'yes, 1' or question == 'yes, one' or question == 'yes one' or question == 'yes 1' or question == 'first' or question == 'liquid' or question == 'liquid foundation':
                                number = 4
                                print (" ")
                                print ("If you are looking for a drugstore option, the Maybelline Fit Me Dewy and Smooth Foundation is good! It is $8 USD, has 24 shades and built in SPF 18.")
                                print (" ")
                                print ("For a mid-priced foundation, the Make Up For Ever Ultra HD Invisible Cover Foundation is the way to go! It is $55 CAD, hydrating, and has 50 shades!")
                                print (" ")
                                print ("Finally, for the high end foundation, the LANCÔME Le Teint Particulier Custom-Made Foundation is great! Although it is $88 CAD, it has over 72,000 shade possibilities.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == '$8 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Fit Me Dewy and Smooth Foundation' or question == 'Fit Me Dewy and Smooth Foundation' or question == 'Maybelline Fit Me Dewy':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Maybelline Fit Me Dewy and Smooth Foundation: https://www.ulta.com/p/fit-me-dewy-smooth-foundation-xlsImpprod2980151")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Make Up For Ever foundation' or question == 'Make Up For Ever' or question == 'Make Up For Ever Ultra HD Invisible Cover Foundation' or question == 'Make Up For Ever' or question == 'Ultra HD Invisible Cover Foundation' or question == 'Ultra HD foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Make Up For Ever Ultra HD Invisible Cover Foundation: https://www.sephora.com/ca/en/product/ultra-hd-invisible-cover-foundation-P398321?om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-79gs3VUGxm.DkZOIPCnUNQ&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-79gs3VUGxm.DkZOIPCnUNQ&ranLinkID=10-1&browserdefault=true")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Lancome foundation' or question == 'Lancome' or question == 'Lancome Le Teint Particulier Custom Made Foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the LANCÔME Le Teint Particulier Custom-Made Foundation: https://www.saksfifthavenue.com/product/cl%C3%A9-de-peau-beaut%C3%A9-radiant-fluid-foundation-matte-broad-spectrum-spf-20-sunscreen-0400012969542.html?ranMID=13816&ranEAID=tv2R4u9rImY&ranSiteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&site_refer=AFF001&mid=13816&siteID=tv2R4u9rImY-shNj8tAYuY7pgVUIe0siPQ&LSoid=894953&LSlinkid=10&LScreativeid=1")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        number = 4
                                        print (" ")
                                        print ("No problem!")
                                        while number == 4:
                                            print (" ")
                                            question = input ("Would you be interested in another type of foundation instead?")
                                            if question == 'yes':
                                                number = 1
                                            elif question == 'no' or question == 'none':
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid response.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'two' or question == 'yes 2' or question == 'yes two' or question == 'yes, 2' or question == 'yes, two' or question == 'second' or question == 'powder' or question == 'powder foundation':
                                number = 4
                                print (" ")
                                print ("Since you have dry skin, I would not recommend purchasing a powder foundation since it will further dry your skin out and flake off throughout the day.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'nope':
                                        print (" ")
                                        number = 2
                                        print ("No problem!")
                                        while number == 2:
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                                else:
                                    print (" ")
                                    print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'three' or question == 'yes 3' or question == 'yes three' or question == 'yes, 3' or question == 'yes, three' or question == 'tinted moisturizer' or question == 'tinted moisturizer foundation' or question == 'third' or question == 'yes third' or question == 'yes, third':
                                number = 4
                                print (" ")
                                print ("If you are looking for a drugstore option, the Neutrogena Protect and Tint tinted moisturizer is good! It is $8.47 USD, has 5 shades and built in SPF 30.")
                                print (" ")
                                print ("For a mid-priced foundation, the Lancôme Feels Good Tinted Moisturizer Sunscreen is the way to go! It is $50 CAD, hydrating, has 15 shades and built in SPF 23 to protect your skin from UV rays!")
                                print (" ")
                                print ("Finally, for the high end foundation, the Trish McEvoy Beauty Balm Instant Solutions is great! Although it is $87 USD, it has built in SPF 35, moisturizer and has 4 shades.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == '$8 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Fit Me Dewy and Smooth Foundation' or question == 'Fit Me Dewy and Smooth Foundation' or question == 'Maybelline Fit Me Dewy':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Neutrogena Protect and Tint tinted moisturizer: https://www.walmart.com/ip/Neutrogena-Protect-Tint-Tinted-Moisturizer-SPF-30-Shade-10-1-1-fl-oz/931175653?irgwc=1&sourceid=imp_zdzST7XA8xyLTlXyX7X%3AOWMEUkBytxUnXy3nWs0&veh=aff&wmlspartner=imp_10078&clickid=zdzST7XA8xyLTlXyX7X%3AOWMEUkBytxUnXy3nWs0&sharedid=womenshealthmag.com&affiliates_ad_id=612734&campaign_id=9383")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Make Up For Ever foundation' or question == 'Make Up For Ever' or question == 'Make Up For Ever Ultra HD Invisible Cover Foundation' or question == 'Make Up For Ever' or question == 'Ultra HD Invisible Cover Foundation' or question == 'Ultra HD foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Lancôme Feels Good Tinted Moisturizer Sunscreen: https://www.sephora.com/ca/en/product/skin-feels-good-skin-nourishing-foundation-P428823")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Lancome foundation' or question == 'Lancome' or question == 'Lancome Le Teint Particulier Custom Made Foundation':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Trish McEvoy Balm Instant Solutions: https://www.trishmcevoy.com/products/beauty-balm-instant-solutions-spf-35?variant=32072318844963")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        print (" ")
                                        question = input ("No problem! Would you be interested in another foundation instead?")
                                        if question == 'yes':
                                            number = 1
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")  
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")                        
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
            else:
                print (" ")
                print ("Sorry, I did not receive any of the options.")
                
       
    elif question == 'lip products' or question == 'lip':
        number = 1
        while number == 1:
            print (" ")
            question = input ("What type of lip products are you looking for? Lip gloss, lipstick or lip liner. Or, are you unsure?")
            if question == 'lip gloss':
                number = 2
                while number == 2:
                    print (" ")
                    question = input ("Do you want a regular or plumping lip gloss?")
                    if question == 'regular' or question == 'regular lip gloss':
                        number = 3
                        print (" ")
                        print ("Regular lip glosses are a cosmetic applied to the lips to provide a glossy finish.")
                        print (" ")
                        print ("For a drusgtore option, the Essence Shine Shine Shine Lip Gloss is great! It is $4 USD, has 13 color options and is very glossy.")
                        print (" ")
                        print ("As a mid-priced option, the Fenty Beauty Gloss Bomb Universal Lip Lumizer is amazing. It is $25 CAD, has 6 color options and has shea butter to moisturize your lips.")
                        print (" ")
                        print ("Finally, for a high end option, the La Prairie Anti-Aging Eye & Lip Perfection is perfect. It is $195 CAD and works as an anti aging eye gel and glossy lip balm.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Essence' or question == 'first' or question == '$4 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Essence Shine Shine Shine Lip Gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Essence Shine Shine Shine Lip Gloss: https://www.ulta.com/p/shine-shine-shine-lipgloss-xlsImpprod16501067?AID=165159&PID=10078&CID=af_165159_10078_&clickId=2T4QLXXiAxyLTlXyX7X%3AOWMEUkBy583OXy3nWs0&SubID=byrdie.com&irgwc=1")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty Gloss Bomb Universal Lip Lumizer' or question == 'Fenty Beauty' or question == 'Fenty Beauty lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Fenty Beauty Gloss Bomb Universal Lip Luminizer: https://www.sephora.com/ca/en/product/gloss-bomb-universal-lip-luminizer-P67988453?skuId=2327260&om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-.ow7c.DgFQMZ0iXUBBrVug&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-.ow7c.DgFQMZ0iXUBBrVug&ranLinkID=10-1&browserdefault=true")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'La Prairie' or question == 'La Prairie Anti-Aging Eye & Lip Perfection' or question == 'La Prairie lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the La Prairie Anti-Aging Eye & Lip Perfection: https://www.nordstrom.com/s/la-prairie-anti-aging-eye-lip-perfection-a-porter-eye-cream-gel-and-lip-balm-compact/3558015?siteid=tv2R4u9rImY-.G9wAjdfQ1IMOJF4sc0tCg&utm_source=rakuten&utm_medium=affiliate&utm_campaign=tv2R4u9rImY&utm_content=1&utm_term=894996&utm_channel=low_nd_affiliates&sp_source=rakuten&sp_campaign=tv2R4u9rImY")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == 'plumping' or question == 'plumping lip gloss':
                        number = 3
                        print (" ")
                        print ("For context, lip plumping glosses are clear or colorful glosses that temporarily make your lips appear more fuller and plumper.")
                        print (" ")
                        print ("For a drusgtore option, the Neutrogena Healthy Lips Plumping Serum is great! It is $13 USD, promotes fuller and plumper looking lips, and also is a great base for lipstick application!")
                        print (" ")
                        print ("As a mid-priced option, the Buxom Full On Plumping Lip Polish Gloss is amazing. It is $28 CAD and has 35 color options in glossy, shimmery and metallic finishes.")
                        print (" ")
                        print ("Finally, for a high end option, the Natura Bissé Diamond Lip Booster is perfect. It is $77 USD, plumps and hydrates lips with ingredients like Omega-5, turmeric oil, vitamin F and capsicum.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Neutrogena' or question == 'first' or question == '$13 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Healthy Lips Plumping Serum' or question == 'Neutrogena Healthy Lips Plumping Serum':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Neutrogena Healthy Lips Plumping Serum: https://www.target.com/p/neutrogena-healthy-lips-plumping-serum-with-peptides-0-5-fl-oz/-/A-76545892")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced lip gloss' or question == 'mid-priced' or question == 'Buxom' or question == 'Buxom Full On Plumping Lip Polish Gloss' or question == 'Buxom lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Buxom Full On Plumping Lip Polish Gloss: https://www.sephora.com/ca/en/product/buxom-full-on-lip-polish-P174213")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Natura Bissé Diamond Lip Booster' or question == 'Natura Bisse' or question == 'Natura Bisse lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Natura Bissé Diamond Lip Booster: https://www.dermstore.com/natura-bisse-diamond-lip-booster/11564670.html")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
                        
            elif question == 'lipstick':
                number = 2
                while number == 2:
                    print (" ")
                    question = input ("Do you want a liquid lipstick or satin lipstick?")
                    if question == 'liquid' or question == 'liquid lipstick':
                        number = 3
                        print (" ")
                        print ("Liquid lipsticks are a cosmetic applied to the lips that contain lipstick pigment and come in different finished like matte or glossy.")
                        print (" ")
                        print ("For a drusgtore option, the Maybelline Superstay Matte Ink Long-Lasting Lipstick is great! It is $10 CAD, has 31 color options, is matte and longlasting.")
                        print (" ")
                        print ("As a mid-priced option, the Stila Stay All Day Liquid Lipstick is amazing. It is $29 CAD, has 15 color options and has a weightless formula that lasts for up to 6 hours of continuous wear.")
                        print (" ")
                        print ("Finally, for a high end option, the CHANEL Rouge Allure Ink Matte Liquid Lip Colour is perfect. It is $40 USD, has 12 colour options, has a matte finish and lasts for 8 hours.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == '$10 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Superstay Matte Ink Long-Lasting Lipstick':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Maybelline Superstay Matte Ink Long-Lasting Lipstick: https://www.walmart.ca/en/ip/maybelline-new-york-superstay-matte-ink-long-lasting-lipstick-5ml-pink/6000197042754")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Stila Stay All Day Liquid Lipstick' or question == 'Stila' or question == 'stila liquid lipstick lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Stila Stay All Day Liquid Lipstick: https://shop.shoppersdrugmart.ca/Luxury/Categories/Makeup/Lips/Lipstick/Stay-all-Day-Liquid-Lipstick/p/LV21")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'La Prairie' or question == 'La Prairie Anti-Aging Eye & Lip Perfection' or question == 'La Prairie lip gloss':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the CHANEL Rouge Allure Ink Matte Liquid Lip Colour: https://www.nordstrom.com/s/chanel-rouge-allure-ink-matte-liquid-lip-colour/4477887")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == 'satin' or question == 'satin lipstick':
                        number = 3
                        print (" ")
                        print ("For context, satin lipsticks are a mix between a glossy and matte finish lipstick. They are very creamy and allow bright colors to pop.")
                        print (" ")
                        print ("For a drusgtore option, the NYX Professional Makeup Shout Loud Satin Lipstick is great! It is $12 CAD, has 24 colour options, and is hydrating.")
                        print (" ")
                        print ("As a mid-priced option, the bareMinerals Mineralist Hydra-Smoothing Lipstick is amazing. It is $26 CAD, has 12 color options, is hydrating and has a satin finish.")
                        print (" ")
                        print ("Finally, for a high end option, the Givenchy Le Rouge Lipstick is perfect. It is $50 CAD, has 19 colour options, is hydrating and long lasting.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these options? If so, which one?")
                            if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'NYX' or question == "nyx" or question == 'first' or question == '$12 option' or question == 'drugstore option' or question == 'drugstore' or question == 'NYX Professional Makeup Shout Loud Satin Lipstick' or question == 'NYX lipstick':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the NYX Professional Makeup Shout Loud Satin Lipstick: https://www.nyxcosmetics.ca/en/-shout-loud-satin-lipstick/NYX_815.html")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced lip gloss' or question == 'mid-priced' or question == 'bareminerals' or question == 'bareMinerals' or question == 'bareMinerals Mineralist Hydra-Smoothing Lipstick' or question == 'bareMinerals lipstick' or question == 'bareminerals lipstick':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the bareMinerals Mineralist Hydra-Smoothing Lipstick: https://www.sephora.com/ca/en/product/bareminerals-mineralist-hydra-smoothing-lipstick-P455324")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Givenchy Le Rouge Lipstick' or question == 'Givenchy' or question == 'givenchy' or question == 'Givenchy lipstick' or question == 'givenchy lipstick':
                                number = 4
                                print (" ")
                                print ("Here is the website to purchase the Givenchy Le Rouge Lipstick: https://www.sephora.com/ca/en/product/le-rouge-P377755")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
                        
            elif question == 'lip liner' or question == 'liner':
                number = 2
                print (" ")
                print ("To explain, lip liners are used to outline the lips and prevent the unwanted spreading of lipstick or lipgloss. They come in a variety of colors and are thin at the tip such that you can precisely line your lips.")
                print (" ")
                print ("For a drusgtore option, the Revlon ColorStay Lipliner is great! It is $12 CAD, has 10 color options and has an 8 hour wear time.")
                print (" ")
                print ("As a mid-priced option, the Lime Crime Angel Lip Liner is amazing. It is $21 CAD, has 10 color options, is cruelty free and vegan.")
                print (" ")
                print ("Finally, for a high end option, the Giorgio Armani Smooth Silk Lip Pencil is perfect. It is $40 CAD, has 4 color options and has a smooth application.")
                while number == 2:
                    print (" ")
                    question = input ("Are you interested in any of these options? If so, which one?")
                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Revlon' or question == 'first' or question == '$12 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Revlon ColorStay Lipliner' or question == 'Revlon lipliner':
                        number = 3
                        print (" ")
                        print ("Here is the website to purchase the Revlon ColorStay Lipliner: https://shop.shoppersdrugmart.ca/Beauty/Categories/Makeup/Lips/Lip-Liner/ColorStay-Lipliner/p/R345?variantCode=309970045463")
                        while number == 3:
                            print (" ")
                            question = input ("Would you like to keep shopping?")
                            if question == 'yes':
                                number = 0
                            elif question == 'no':
                                print (" ")
                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                number = 'done'
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced foundation' or question == 'mid-priced' or question == 'Fenty Beauty Gloss Bomb Universal Lip Lumizer' or question == 'Fenty Beauty' or question == 'Fenty Beauty lip gloss':
                        number = 3
                        print (" ")
                        print ("Here is the website to purchase the Lime Crime Angel Lip Liner: https://limecrime.com/products/apricot-nude-lip-liner")
                        while number == 3:
                            print (" ")
                            question = input ("Would you like to keep shopping?")
                            if question == 'yes':
                                number = 0
                            elif question == 'no':
                                print (" ")
                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                number = 'done'
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'La Prairie' or question == 'La Prairie Anti-Aging Eye & Lip Perfection' or question == 'La Prairie lip gloss':
                        number = 3
                        print (" ")
                        print ("Here is the website to purchase the Giorgio Armani Smooth Silk Lip Pencil: https://www.nordstrom.ca/s/giorgio-armani-smooth-silk-lip-pencil/3008470")
                        while number == 3:
                            print (" ")
                            question = input ("Would you like to keep shopping?")
                            if question == 'yes':
                                number = 0
                            elif question == 'no':
                                print (" ")
                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                number = 'done'
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == 'none' or question == 'no':
                        number = 3
                        print (" ")
                        print ("No problem!")
                        while number == 3:
                            print (" ")
                            question = input ("Would you be interested in another type of lip product instead?")
                            if question == 'yes':
                                number = 1
                            elif question == 'no' or question == 'none':
                                number = 4
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you like to keep shopping?")
                                    if question == 'yes':
                                        number = 0
                                    elif question == 'no':
                                        print (" ")
                                        print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                        number = 'done'
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid response.")
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
            elif question == 'unsure' or question == 'need help' or question == 'help':
                number = 2
                print (" ")
                print ("No problem!")
                while number == 2:
                    print (" ")
                    question = input ("Do you want a transparent or opaque lip product?")
                    if question == 'transparent' or question == 'transparent lip product':
                        number = 3
                        print (" ")
                        print ("For context, regular lip glosses are a transparent cosmetic applied to the lips to provide a glossy finish.")
                        print (" ")
                        print ("Plumping lip glosses have the same transparent finish but they make your lips look fuller.")                  
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these lip glosses?")
                            if question == '1' or question == 'one' or question == 'yes, 1' or question == 'yes, one' or question == 'yes one' or question == 'yes 1' or question == 'first' or question == 'regular' or question == 'regular lip glosses' or question == 'regular lip gloss':
                                number = 4
                                print (" ")
                                print ("For a drusgtore option, the Essence Shine Shine Shine Lip Gloss is great! It is $4 USD, has 13 color options and is very glossy.")
                                print (" ")
                                print ("As a mid-priced option, the Fenty Beauty Gloss Bomb Universal Lip Lumizer is amazing. It is $25 CAD, has 6 color options and has shea butter to moisturize your lips.")
                                print (" ")
                                print ("Finally, for a high end option, the La Prairie Anti-Aging Eye & Lip Perfection is perfect. It is $195 CAD and works as an anti aging eye gel and glossy lip balm.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes, first' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'one' or question == 'Essence' or question == 'first' or question == '$4 option' or question == 'drugstore option' or question == 'drugstore' or question == 'Essence Shine Shine Shine Lip Gloss' or question == 'Essence lip gloss' or question == 'essence lip gloss':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Essence Shine Shine Shine Lip Gloss: https://www.ulta.com/p/shine-shine-shine-lipgloss-xlsImpprod16501067?AID=165159&PID=10078&CID=af_165159_10078_&clickId=2T4QLXXiAxyLTlXyX7X%3AOWMEUkBy583OXy3nWs0&SubID=byrdie.com&irgwc=1")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid-priced lip gloss' or question == 'mid-priced' or question == 'Fenty Beauty lip gloss' or question == 'Fenty Beauty' or question == 'Fenty Beauty Gloss Bomb Universal Lip Lumizer' or question == 'Fenty':
                                        print (" ")
                                        print ("Here is the website to purchase the Fenty Beauty Gloss Bomb Universal Lip Lumizer: https://www.sephora.com/ca/en/product/gloss-bomb-universal-lip-luminizer-P67988453?skuId=2327260&om_mmc=aff-linkshare-redirect-tv2R4u9rImY&c3ch=Linkshare&c3nid=tv2R4u9rImY&affid=tv2R4u9rImY-.ow7c.DgFQMZ0iXUBBrVug&ranEAID=tv2R4u9rImY&ranMID=2417&ranSiteID=tv2R4u9rImY-.ow7c.DgFQMZ0iXUBBrVug&ranLinkID=10-1&browserdefault=true")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'three' or question == 'high end lip gloss' or question == 'high-end' or question == 'La Prairie Anti-Aging Eye & Lip Perfection' or question == 'La Prairie' or question == 'La Prairie lip gloss' or question == 'la prairie lip gloss':
                                        print (" ")
                                        print ("Here is the website to purchase the La Prairie Anti-Aging Eye & Lip Perfection: https://www.nordstrom.com/s/la-prairie-anti-aging-eye-lip-perfection-a-porter-eye-cream-gel-and-lip-balm-compact/3558015?siteid=tv2R4u9rImY-.G9wAjdfQ1IMOJF4sc0tCg&utm_source=rakuten&utm_medium=affiliate&utm_campaign=tv2R4u9rImY&utm_content=1&utm_term=894996&utm_channel=low_nd_affiliates&sp_source=rakuten&sp_campaign=tv2R4u9rImY")
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        number = 4
                                        print (" ")
                                        print ("No problem!")
                                        while number == 4:
                                            print (" ")
                                            question = input ("Would you be interested in another type of lip product instead?")
                                            if question == 'yes':
                                                number = 1
                                            elif question == 'no' or question == 'none':
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid response.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'two' or question == 'yes 2' or question == 'yes two' or question == 'yes, 2' or question == 'yes, two' or question == 'second' or question == 'plumping' or question == 'plumping lip gloss':
                                number = 4
                                print (" ")
                                print ("For a drusgtore option, the Neutrogena Healthy Lips Plumping Serum is great! It is $13 USD, promotes fuller and plumper looking lips, and also is a great base for lipstick application!")
                                print (" ")
                                print ("As a mid-priced option, the Buxom Full On Plumping Lip Polish Gloss is amazing. It is $28 CAD and has 35 color options in glossy, shimmery and metallic finishes.")
                                print (" ")
                                print ("Finally, for a high end option, the Natura Bissé Diamond Lip Booster is perfect. It is $77 USD, plumps and hydrates lips with ingredients like Omega-5, turmeric oil, vitamin F and capsicum.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'first' or question == 'Neutrogena' or question == 'Neutrogena Healthy Lips Plumping Serum' or question == 'yes, 1' or question == 'yes 1' or question == 'yes, first' or question == 'yes first' or question == 'one' or question == 'yes one' or question == 'yes, one' or question == 'drugstore option' or question == 'drugstore':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Neutrogena Healthy Lips Plumping Serum: https://www.target.com/p/neutrogena-healthy-lips-plumping-serum-with-peptides-0-5-fl-oz/-/A-76545892")
                                        while number == 5:
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'buxom' or question == 'Buxom' or question == 'Buxom lip gloss' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid priced lip gloss' or question == 'mid priced' or question == 'Buxom Full On Plumping Lip Polish Gloss':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Buxom Full On Plumping Lip Polish Gloss: https://www.sephora.com/ca/en/product/buxom-full-on-lip-polish-P174213")
                                        while number == 5:
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Natura Bissé Diamond Lip Booster' or question == 'Natura Bisse' or question == 'Natura Bisse lip gloss':
                                        number = 5
                                        print ("Here is the website to purchase the Natura Bissé Diamond Lip Booster: https://www.dermstore.com/natura-bisse-diamond-lip-booster/11564670.html")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'no' or question == 'none':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")
                    elif question == 'opaque' or question == 'opaque lip product':
                        number = 3
                        print (" ")
                        print ("For context, liquid lipsticks are a cosmetic applied to the lips that contain lipstick pigment and come in different finished like matte or glossy.")
                        print (" ")
                        print ("Satin lipsticks are a mix between a glossy and matte finish lipstick. They are very creamy and allow bright colors to pop.")
                        print (" ")
                        print ("Finally, lip liners are used to outline the lips and prevent the unwanted spreading of lipstick or lipgloss. They come in a variety of colors and are thin at the tip such that you can precisely line your lips.")
                        while number == 3:
                            print (" ")
                            question = input ("Are you interested in any of these types of lip products?")
                            if question == '1' or question == 'one' or question == 'yes, 1' or question == 'yes, one' or question == 'yes one' or question == 'yes 1' or question == 'first' or question == 'liquid' or question == 'liquid lipstick' or question == 'liquid lipsticks':
                                number = 4
                                print (" ")
                                print ("For a drusgtore option, the Maybelline Superstay Matte Ink Long-Lasting Lipstick is great! It is $10 CAD, has 31 color options, is matte and longlasting.")
                                print (" ")
                                print ("As a mid-priced option, the Stila Stay All Day Liquid Lipstick is amazing. It is $29 CAD, has 15 color options and has a weightless formula that lasts for up to 6 hours of continuous wear.")
                                print (" ")
                                print ("Finally, for a high end option, the CHANEL Rouge Allure Ink Matte Liquid Lip Colour is perfect. It is $40 USD, has 12 colour options, has a matte finish and lasts for 8 hours.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Maybelline' or question == 'first' or question == 'drugstore option' or question == 'drugstore' or question == 'Maybelline Superstay Matte Ink Long-Lasting Lipstick' or question == 'Superstay Matte Ink Long-Lasting Lipstick' or question == 'Maybelline lipstick' or question == 'Maybelline liquid lipstick':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Maybelline Superstay Matte Ink Long-Lasting Lipstick: https://www.walmart.ca/en/ip/maybelline-new-york-superstay-matte-ink-long-lasting-lipstick-5ml-pink/6000197042754")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid priced lipstick' or question == 'mid priced liquid lipstick' or question == 'mid priced' or question == 'stila liquid lipstick' or question == 'Stila' or question == 'Stila Stay All Day Liquid Lipstick' or question == 'Stay All Day Liquid Lipstick':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Stila Stay All Day Liquid Lipstick: https://shop.shoppersdrugmart.ca/Luxury/Categories/Makeup/Lips/Lipstick/Stay-all-Day-Liquid-Lipstick/p/LV21")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'chanel lipstick' or question == 'CHANEL lipstick' or question == 'chanel liquid lipstick' or question == 'CHANEL liquid lipstick' or question == 'CHANEL' or question == 'chanel' or question == 'CHANEL Rouge Allure Ink Matte Liquid Lip Colour':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the CHANEL Rouge Allure Ink Matte Liquid Lip Colour: https://www.nordstrom.com/s/chanel-rouge-allure-ink-matte-liquid-lip-colour/4477887")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        number = 4
                                        print (" ")
                                        print ("No problem!")
                                        while number == 4:
                                            print (" ")
                                            question = input ("Would you be interested in another type of foundation instead?")
                                            if question == 'yes':
                                                number = 1
                                            elif question == 'no' or question == 'none':
                                                print (" ")
                                                question = input ("Would you like to keep shopping?")
                                                if question == 'yes':
                                                    number = 0
                                                elif question == 'no':
                                                    print (" ")
                                                    print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                    number = 'done'
                                                else:
                                                    print (" ")
                                                    print ("Sorry, I did not receive a valid option.")
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid response.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == '2' or question == 'two' or question == 'yes 2' or question == 'yes two' or question == 'yes, 2' or question == 'yes, two' or question == 'satin' or question == 'satin lipstick' or question == 'second' or question == 'yes second' or question == 'yes, second':
                                number = 4
                                print (" ")
                                print ("For a drusgtore option, the NYX Professional Makeup Shout Loud Satin Lipstick is great! It is $12 CAD, has 24 colour options, and is hydrating.")
                                print (" ")
                                print ("As a mid-priced option, the bareMinerals Mineralist Hydra-Smoothing Lipstick is amazing. It is $26 CAD, has 12 color options, is hydrating and has a satin finish.")
                                print (" ")
                                print ("Finally, for a high end option, the Givenchy Le Rouge Lipstick is perfect. It is $50 CAD, has 19 colour options, is hydrating and long lasting.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'NYX' or question == 'nyx' or question == 'first' or question == 'drugstore option' or question == 'drugstore' or question == 'NYX Professional Makeup Shout Loud Satin Lipstick' or question == 'Professional Makeup Shout Loud Satin Lipstick' or question == 'NYX lipstick' or question == 'nyx lipstick' or question == 'NYX satin lipstick' or question == 'nyx satin lipstick':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the NYX Professional Makeup Shout Loud Satin Lipstick: https://www.nyxcosmetics.ca/en/-shout-loud-satin-lipstick/NYX_815.html")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid priced satin lipstick' or question == 'mid priced lipstick' or question == 'mid priced' or question == 'bareMinerals Mineralist Hydra-Smoothing Lipstick' or question == 'bareMinerals Mineralist' or question == 'bareMinerals satin lipstick' or question == 'bareminerals satin lipstick' or question == 'bareMinerals lipstick' or question == 'bareminerals lipstick':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the bareMinerals Mineralist Hydra-Smoothing Lipstick: https://www.sephora.com/ca/en/product/bareminerals-mineralist-hydra-smoothing-lipstick-P455324")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Givenchy Le Rouge Lipstick' or question == 'Givenchy' or question == 'givenchy':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Givenchy Le Rouge Lipstick: https://www.sephora.com/ca/en/product/le-rouge-P377755")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        print (" ")
                                        question = input ("No problem! Would you be interested in another foundation instead?")
                                        if question == 'yes':
                                            number = 1
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of foundation instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")  
                                else:
                                    print (" ")
                                    print ("Sorry, I did not receive a valid option.")
                            elif question == '3' or question == 'three' or question == 'yes 3' or question == 'yes three' or question == 'yes, 3' or question == 'yes, three' or question == 'lip liner' or question == 'liner' or question == 'lip liner lip product' or question == 'third' or question == 'yes third' or question == 'yes, third':
                                number = 4
                                print (" ")
                                print ("For a drusgtore option, the Revlon ColorStay Lipliner is great! It is $12 CAD, has 10 color options and has an 8 hour wear time.")
                                print (" ")
                                print ("As a mid-priced option, the Lime Crime Angel Lip Liner is amazing. It is $21 CAD, has 10 color options, is cruelty free and vegan.")
                                print (" ")
                                print ("Finally, for a high end option, the Giorgio Armani Smooth Silk Lip Pencil is perfect. It is $40 CAD, has 4 color options and has a smooth application.")
                                while number == 4:
                                    print (" ")
                                    question = input ("Are you interested in any of these options? If so, which one?")
                                    if question == '1' or question == 'yes one' or question == 'yes 1' or question == 'yes, 1' or question == 'yes, first' or question == 'one' or question == 'Revlon' or question == 'revlon' or question == 'first' or question == 'drugstore option' or question == 'drugstore' or question == 'Revlon ColorStay Lipliner' or question == 'ColorStay Lipliner':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Revlon ColorStay Lipliner: https://shop.shoppersdrugmart.ca/Beauty/Categories/Makeup/Lips/Lip-Liner/ColorStay-Lipliner/p/R345?variantCode=309970045463")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '2' or question == 'yes two' or question == 'yes 2' or question == 'yes, 2' or question == 'second' or question == 'two' or question == 'mid priced lip liner' or question == 'mid priced' or question == 'Lime Crime Angel Lip Liner' or question == 'Lime Crime' or question == 'lime crime lip liner' or question == 'Lime Crime lip liner':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Lime Crime Angel Lip Liner: https://limecrime.com/products/apricot-nude-lip-liner")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == '3' or question == 'yes three' or question == 'yes 3' or question == 'yes, 3' or question == 'third' or question == 'high end' or question == 'three' or question == 'Giorgio Armani Smooth Silk Lip Pencil' or question == 'giorgio armani' or question == 'Giorgio Armani' or question == 'Giorgio Armani lip liner' or question == 'giorio armani lip liner' or question == 'Giorgio' or question == 'giorgio' or question == 'Armani' or question == 'armani':
                                        number = 5
                                        print (" ")
                                        print ("Here is the website to purchase the Giorgio Armani Smooth Silk Lip Pencil: https://www.nordstrom.ca/s/giorgio-armani-smooth-silk-lip-pencil/3008470")
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    elif question == 'none' or question == 'no':
                                        print (" ")
                                        question = input ("No problem! Would you be interested in another lip product instead?")
                                        if question == 'yes':
                                            number = 1
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid option.")
                            elif question == 'none' or question == 'no':
                                number = 4
                                print (" ")
                                print ("No problem!")
                                while number == 4:
                                    print (" ")
                                    question = input ("Would you be interested in another type of lip product instead?")
                                    if question == 'yes':
                                        number = 1
                                    elif question == 'no' or question == 'none':
                                        number = 5
                                        while number == 5:
                                            print (" ")
                                            question = input ("Would you like to keep shopping?")
                                            if question == 'yes':
                                                number = 0
                                            elif question == 'no':
                                                print (" ")
                                                print ("No problem! Thank you for visiting Makeup.ca and I hope to see you again soon!")
                                                number = 'done'
                                            else:
                                                print (" ")
                                                print ("Sorry, I did not receive a valid option.")
                                    else:
                                        print (" ")
                                        print ("Sorry, I did not receive a valid response.")  
                            else:
                                print (" ")
                                print ("Sorry, I did not receive a valid option.")                        
                    else:
                        print (" ")
                        print ("Sorry, I did not receive a valid option.")
            else:
                print (" ")
                print ("Sorry, I did not receive any of the options.")
    else:
        print (" ")
        print ("Sorry, I did not receive any of the options.")
        number = 0
