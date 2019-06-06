import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' 
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') 
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://username:password@localhost/databasename' 
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mssql+pymssql://username:password@hostname/databasename'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # eMail config
    MAIL_SERVER = 'emailhostname'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    ADMINS = ['email@email.com']

    #Pagination
    PROJECTS_PER_PAGE = 50

    TENDER_SCHEMA = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "SenderID",
    "ReceiverID",
    "TenderedDate",
    "TenderedTime",
    "SCAC",
    "BillOfLading",
    "PaymentMethod",
    "TenderStatus",
    "TotalPieces",
    "TotalWeight",
    "ReferenceNumbers",
    "RespondBy",
    "Comments",
    "HeaderLocations",
    "Equipment",
    "Stops"
  ],
  "properties": {
    "SenderID": {
      "$id": "#/properties/SenderID",
      "type": "string",
      "title": "The Senderid Schema",
      "default": "",
      "examples": [
        "receiver"
      ],
      "pattern": "^(.*)$"
    },
    "ReceiverID": {
      "$id": "#/properties/ReceiverID",
      "type": "string",
      "title": "The Receiverid Schema",
      "default": "",
      "examples": [
        "sender"
      ],
      "pattern": "^(.*)$"
    },
    "TenderedDate": {
      "$id": "#/properties/TenderedDate",
      "type": "string",
      "title": "The Tendereddate Schema",
      "default": "",
      "examples": [
        "20190505"
      ],
      "pattern": "^(.*)$"
    },
    "TenderedTime": {
      "$id": "#/properties/TenderedTime",
      "type": "string",
      "title": "The Tenderedtime Schema",
      "default": "",
      "examples": [
        "2324"
      ],
      "pattern": "^(.*)$"
    },
    "SCAC": {
      "$id": "#/properties/SCAC",
      "type": "string",
      "title": "The Scac Schema",
      "default": "",
      "examples": [
        "SCAC"
      ],
      "pattern": "^(.*)$"
    },
    "BillOfLading": {
      "$id": "#/properties/BillOfLading",
      "type": "string",
      "title": "The Billoflading Schema",
      "default": "",
      "examples": [
        "65788540"
      ],
      "pattern": "^(.*)$"
    },
    "PaymentMethod": {
      "$id": "#/properties/PaymentMethod",
      "type": "string",
      "title": "The Paymentmethod Schema",
      "default": "",
      "examples": [
        "PP"
      ],
      "pattern": "^(.*)$"
    },
    "TenderStatus": {
      "$id": "#/properties/TenderStatus",
      "type": "string",
      "title": "The Tenderstatus Schema",
      "default": "",
      "examples": [
        "00"
      ],
      "pattern": "^(.*)$"
    },
    "TotalPieces": {
      "$id": "#/properties/TotalPieces",
      "type": "string",
      "title": "The Totalpieces Schema",
      "default": "",
      "examples": [
        "2784"
      ],
      "pattern": "^(.*)$"
    },
    "TotalWeight": {
      "$id": "#/properties/TotalWeight",
      "type": "string",
      "title": "The Totalweight Schema",
      "default": "",
      "examples": [
        "32547"
      ],
      "pattern": "^(.*)$"
    },
    "ReferenceNumbers": {
      "$id": "#/properties/ReferenceNumbers",
      "type": "array",
      "title": "The Referencenumbers Schema",
      "items": {
        "$id": "#/properties/ReferenceNumbers/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "Type",
          "ReferenceNumber"
        ],
        "properties": {
          "Type": {
            "$id": "#/properties/ReferenceNumbers/items/properties/Type",
            "type": "string",
            "title": "The Type Schema",
            "default": "",
            "examples": [
              "PO"
            ],
            "pattern": "^(.*)$"
          },
          "ReferenceNumber": {
            "$id": "#/properties/ReferenceNumbers/items/properties/ReferenceNumber",
            "type": "string",
            "title": "The Referencenumber Schema",
            "default": "",
            "examples": [
              "123456789"
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "RespondBy": {
      "$id": "#/properties/RespondBy",
      "type": "object",
      "title": "The Respondby Schema",
      "required": [
        "Date",
        "Time",
        "TimeZone"
      ],
      "properties": {
        "Date": {
          "$id": "#/properties/RespondBy/properties/Date",
          "type": "string",
          "title": "The Date Schema",
          "default": "",
          "examples": [
            "20190506"
          ],
          "pattern": "^(.*)$"
        },
        "Time": {
          "$id": "#/properties/RespondBy/properties/Time",
          "type": "string",
          "title": "The Time Schema",
          "default": "",
          "examples": [
            "0800"
          ],
          "pattern": "^(.*)$"
        },
        "TimeZone": {
          "$id": "#/properties/RespondBy/properties/TimeZone",
          "type": "string",
          "title": "The Timezone Schema",
          "default": "",
          "examples": [
            "CT"
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "Comments": {
      "$id": "#/properties/Comments",
      "type": "array",
      "title": "The Comments Schema",
      "items": {
        "$id": "#/properties/Comments/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "Comment"
        ],
        "properties": {
          "Comment": {
            "$id": "#/properties/Comments/items/properties/Comment",
            "type": "string",
            "title": "The Comment Schema",
            "default": "",
            "examples": [
              "aaaaaaaaaaaaaaaaaaaaaaaaaa"
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "HeaderLocations": {
      "$id": "#/properties/HeaderLocations",
      "type": "array",
      "title": "The Headerlocations Schema",
      "items": {
        "$id": "#/properties/HeaderLocations/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "Type",
          "Name",
          "ID",
          "Address",
          "City",
          "State",
          "ZipCode",
          "Country"
        ],
        "properties": {
          "Type": {
            "$id": "#/properties/HeaderLocations/items/properties/Type",
            "type": "string",
            "title": "The Type Schema",
            "default": "",
            "examples": [
              "BT"
            ],
            "pattern": "^(.*)$"
          },
          "Name": {
            "$id": "#/properties/HeaderLocations/items/properties/Name",
            "type": "string",
            "title": "The Name Schema",
            "default": "",
            "examples": [
              "SOme Stores Inc"
            ],
            "pattern": "^(.*)$"
          },
          "ID": {
            "$id": "#/properties/HeaderLocations/items/properties/ID",
            "type": "string",
            "title": "The Id Schema",
            "default": "",
            "examples": [
              "0078742000008"
            ],
            "pattern": "^(.*)$"
          },
          "Address": {
            "$id": "#/properties/HeaderLocations/items/properties/Address",
            "type": "string",
            "title": "The Address Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "City": {
            "$id": "#/properties/HeaderLocations/items/properties/City",
            "type": "string",
            "title": "The City Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "State": {
            "$id": "#/properties/HeaderLocations/items/properties/State",
            "type": "string",
            "title": "The State Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "ZipCode": {
            "$id": "#/properties/HeaderLocations/items/properties/ZipCode",
            "type": "string",
            "title": "The Zipcode Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "Country": {
            "$id": "#/properties/HeaderLocations/items/properties/Country",
            "type": "string",
            "title": "The Country Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "Equipment": {
      "$id": "#/properties/Equipment",
      "type": "object",
      "title": "The Equipment Schema",
      "required": [
        "Initial",
        "TrailerNumber",
        "TrailerType",
        "TrailerSize"
      ],
      "properties": {
        "Initial": {
          "$id": "#/properties/Equipment/properties/Initial",
          "type": "string",
          "title": "The Initial Schema",
          "default": "",
          "examples": [
            "WC"
          ],
          "pattern": "^(.*)$"
        },
        "TrailerNumber": {
          "$id": "#/properties/Equipment/properties/TrailerNumber",
          "type": "string",
          "title": "The Trailernumber Schema",
          "default": "",
          "examples": [
            "90012"
          ],
          "pattern": "^(.*)$"
        },
        "TrailerType": {
          "$id": "#/properties/Equipment/properties/TrailerType",
          "type": "string",
          "title": "The Trailertype Schema",
          "default": "",
          "examples": [
            "TF"
          ],
          "pattern": "^(.*)$"
        },
        "TrailerSize": {
          "$id": "#/properties/Equipment/properties/TrailerSize",
          "type": "string",
          "title": "The Trailersize Schema",
          "default": "",
          "examples": [
            "5300"
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "Stops": {
      "$id": "#/properties/Stops",
      "type": "array",
      "title": "The Stops Schema",
      "items": {
        "$id": "#/properties/Stops/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "StopInfo",
          "ContactInfo",
          "AppointmentInfo",
          "StopReferenceNumbers",
          "OIDNumbers"
        ],
        "properties": {
          "StopInfo": {
            "$id": "#/properties/Stops/items/properties/StopInfo",
            "type": "object",
            "title": "The Stopinfo Schema",
            "required": [
              "StopNumber",
              "StopType",
              "StopName",
              "StopAddress",
              "StopCity",
              "StopState",
              "StopZip",
              "StopCountry",
              "StopID"
            ],
            "properties": {
              "StopNumber": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopNumber",
                "type": "string",
                "title": "The Stopnumber Schema",
                "default": "",
                "examples": [
                  "1"
                ],
                "pattern": "^(.*)$"
              },
              "StopType": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopType",
                "type": "string",
                "title": "The Stoptype Schema",
                "default": "",
                "examples": [
                  "SF"
                ],
                "pattern": "^(.*)$"
              },
              "StopName": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopName",
                "type": "string",
                "title": "The Stopname Schema",
                "default": "",
                "examples": [
                  "BAYTOWN WIDGETS"
                ],
                "pattern": "^(.*)$"
              },
              "StopAddress": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopAddress",
                "type": "string",
                "title": "The Stopaddress Schema",
                "default": "",
                "examples": [
                  "4554 OSCAR NELSON JR DR"
                ],
                "pattern": "^(.*)$"
              },
              "StopCity": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopCity",
                "type": "string",
                "title": "The Stopcity Schema",
                "default": "",
                "examples": [
                  "BAYTOWN"
                ],
                "pattern": "^(.*)$"
              },
              "StopState": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopState",
                "type": "string",
                "title": "The Stopstate Schema",
                "default": "",
                "examples": [
                  "TX"
                ],
                "pattern": "^(.*)$"
              },
              "StopZip": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopZip",
                "type": "string",
                "title": "The Stopzip Schema",
                "default": "",
                "examples": [
                  "77523"
                ],
                "pattern": "^(.*)$"
              },
              "StopCountry": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopCountry",
                "type": "string",
                "title": "The Stopcountry Schema",
                "default": "",
                "examples": [
                  "USA"
                ],
                "pattern": "^(.*)$"
              },
              "StopID": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopID",
                "type": "string",
                "title": "The Stopid Schema",
                "default": "",
                "examples": [
                  "91515709"
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "ContactInfo": {
            "$id": "#/properties/Stops/items/properties/ContactInfo",
            "type": "object",
            "title": "The Contactinfo Schema",
            "required": [
              "Name",
              "Phone",
              "Email"
            ],
            "properties": {
              "Name": {
                "$id": "#/properties/Stops/items/properties/ContactInfo/properties/Name",
                "type": "string",
                "title": "The Name Schema",
                "default": "",
                "examples": [
                  "MONTE PYTHON"
                ],
                "pattern": "^(.*)$"
              },
              "Phone": {
                "$id": "#/properties/Stops/items/properties/ContactInfo/properties/Phone",
                "type": "string",
                "title": "The Phone Schema",
                "default": "",
                "examples": [
                  "5554561234"
                ],
                "pattern": "^(.*)$"
              },
              "Email": {
                "$id": "#/properties/Stops/items/properties/ContactInfo/properties/Email",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "AppointmentInfo": {
            "$id": "#/properties/Stops/items/properties/AppointmentInfo",
            "type": "object",
            "title": "The Appointmentinfo Schema",
            "required": [
              "EarlyDate",
              "EarlyTime",
              "EarlyTimeZone",
              "LateDate",
              "LateTime",
              "LateTimeZone"
            ],
            "properties": {
              "EarlyDate": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/EarlyDate",
                "type": "string",
                "title": "The Earlydate Schema",
                "default": "",
                "examples": [
                  "20190505"
                ],
                "pattern": "^(.*)$"
              },
              "EarlyTime": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/EarlyTime",
                "type": "string",
                "title": "The Earlytime Schema",
                "default": "",
                "examples": [
                  "2315"
                ],
                "pattern": "^(.*)$"
              },
              "EarlyTimeZone": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/EarlyTimeZone",
                "type": "string",
                "title": "The Earlytimezone Schema",
                "default": "",
                "examples": [
                  "CT"
                ],
                "pattern": "^(.*)$"
              },
              "LateDate": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateDate",
                "type": "string",
                "title": "The Latedate Schema",
                "default": "",
                "examples": [
                  "20190505"
                ],
                "pattern": "^(.*)$"
              },
              "LateTime": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateTime",
                "type": "string",
                "title": "The Latetime Schema",
                "default": "",
                "examples": [
                  "2315"
                ],
                "pattern": "^(.*)$"
              },
              "LateTimeZone": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateTimeZone",
                "type": "string",
                "title": "The Latetimezone Schema",
                "default": "",
                "examples": [
                  "CT"
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "StopReferenceNumbers": {
            "$id": "#/properties/Stops/items/properties/StopReferenceNumbers",
            "type": "array",
            "title": "The Stopreferencenumbers Schema",
            "items": {
              "$id": "#/properties/Stops/items/properties/StopReferenceNumbers/items",
              "type": "object",
              "title": "The Items Schema",
              "required": [
                "Type",
                "ReferenceNumber"
              ],
              "properties": {
                "Type": {
                  "$id": "#/properties/Stops/items/properties/StopReferenceNumbers/items/properties/Type",
                  "type": "string",
                  "title": "The Type Schema",
                  "default": "",
                  "examples": [
                    "PO"
                  ],
                  "pattern": "^(.*)$"
                },
                "ReferenceNumber": {
                  "$id": "#/properties/Stops/items/properties/StopReferenceNumbers/items/properties/ReferenceNumber",
                  "type": "string",
                  "title": "The Referencenumber Schema",
                  "default": "",
                  "examples": [
                    "123456789"
                  ],
                  "pattern": "^(.*)$"
                }
              }
            }
          },
          "OIDNumbers": {
            "$id": "#/properties/Stops/items/properties/OIDNumbers",
            "type": "array",
            "title": "The Oidnumbers Schema",
            "items": {
              "$id": "#/properties/Stops/items/properties/OIDNumbers/items",
              "type": "object",
              "title": "The Items Schema",
              "required": [
                "RefID",
                "PO",
                "Pieces",
                "Weight",
                "Volume"
              ],
              "properties": {
                "RefID": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/RefID",
                  "type": "string",
                  "title": "The Refid Schema",
                  "default": "",
                  "examples": [
                    "28"
                  ],
                  "pattern": "^(.*)$"
                },
                "PO": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/PO",
                  "type": "string",
                  "title": "The Po Schema",
                  "default": "",
                  "examples": [
                    "0815197030"
                  ],
                  "pattern": "^(.*)$"
                },
                "Pieces": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Pieces",
                  "type": "string",
                  "title": "The Pieces Schema",
                  "default": "",
                  "examples": [
                    "3"
                  ],
                  "pattern": "^(.*)$"
                },
                "Weight": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Weight",
                  "type": "string",
                  "title": "The Weight Schema",
                  "default": "",
                  "examples": [
                    "5361"
                  ],
                  "pattern": "^(.*)$"
                },
                "Volume": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Volume",
                  "type": "string",
                  "title": "The Volume Schema",
                  "default": "",
                  "examples": [
                    "102"
                  ],
                  "pattern": "^(.*)$"
                }
              }
            }
          }
        }
      }
    }
  }
}