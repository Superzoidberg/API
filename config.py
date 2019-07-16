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
    "Hazmat",
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
      "pattern": "^(.{1,15})$"
    },
    "ReceiverID": {
      "$id": "#/properties/ReceiverID",
      "type": "string",
      "title": "The Receiverid Schema",
      "default": "",
      "examples": [
        "sender"
      ],
      "pattern": "^(.{1,15})$"
    },
    "TenderedDate": {
      "$id": "#/properties/TenderedDate",
      "type": "string",
      "title": "The Tendereddate Schema",
      "default": "",
      "examples": [
        "20190505"
      ],
      "pattern": "^([0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9])$"
    },
    "TenderedTime": {
      "$id": "#/properties/TenderedTime",
      "type": "string",
      "title": "The Tenderedtime Schema",
      "default": "",
      "examples": [
        "2324"
      ],
      "pattern": "^([0-2][0-9][0-5][0-9])$"
    },
    "SCAC": {
      "$id": "#/properties/SCAC",
      "type": "string",
      "title": "The Scac Schema",
      "default": "",
      "examples": [
        "SCAC"
      ],
      "pattern": "^(\D{4})$"
    },
    "BillOfLading": {
      "$id": "#/properties/BillOfLading",
      "type": "string",
      "title": "The Billoflading Schema",
      "default": "",
      "examples": [
        "65788540"
      ],
      "pattern": "^(.{1,30})$"
    },
    "PaymentMethod": {
      "$id": "#/properties/PaymentMethod",
      "type": "string",
      "title": "The Paymentmethod Schema",
      "default": "",
      "examples": [
        "PP",
        "CC"
      ],
      "pattern": "^(CC|PP)$"
    },
    "TenderStatus": {
      "$id": "#/properties/TenderStatus",
      "type": "string",
      "title": "The Tenderstatus Schema",
      "default": "",
      "examples": [
        "00"
      ],
      "pattern": "^(\d{2})$"
    },
    "TotalPieces": {
      "$id": "#/properties/TotalPieces",
      "type": "string",
      "title": "The Totalpieces Schema",
      "default": "",
      "examples": [
        "2784"
      ],
      "pattern": "^(\d{0,5})$"
    },
    "TotalWeight": {
      "$id": "#/properties/TotalWeight",
      "type": "string",
      "title": "The Totalweight Schema",
      "default": "",
      "examples": [
        "32547"
      ],
      "pattern": "^(\d{0,5})$"
    },
    "Hazmat": {
      "$id": "#/properties/Hazmat",
      "type": "string",
      "title": "The Hazmat Schema",
      "default": "",
      "examples": [
        "Y",
        "N"
      ],
      "pattern": "^([Y|N])$"
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
            "pattern": "^(^$|\D{2,3})$"
          },
          "ReferenceNumber": {
            "$id": "#/properties/ReferenceNumbers/items/properties/ReferenceNumber",
            "type": "string",
            "title": "The Referencenumber Schema",
            "default": "",
            "examples": [
              "123456789"
            ],
            "pattern": "^(^$|.{1,30})$"
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
          "pattern": "^([0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9])$"
        },
        "Time": {
          "$id": "#/properties/RespondBy/properties/Time",
          "type": "string",
          "title": "The Time Schema",
          "default": "",
          "examples": [
            "0800"
          ],
          "pattern": "^([0-2][0-9][0-5][0-9])$"
        },
        "TimeZone": {
          "$id": "#/properties/RespondBy/properties/TimeZone",
          "type": "string",
          "title": "The Timezone Schema",
          "default": "",
          "examples": [
            "CT"
          ],
          "pattern": "^(\D{2})$"
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
            "pattern": "^(^$|.{0,45})$"
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
            "pattern": "^(\D{2})$"
          },
          "Name": {
            "$id": "#/properties/HeaderLocations/items/properties/Name",
            "type": "string",
            "title": "The Name Schema",
            "default": "",
            "examples": [
              "SOme Stores Inc"
            ],
            "pattern": "^(.{0,25})$"
          },
          "ID": {
            "$id": "#/properties/HeaderLocations/items/properties/ID",
            "type": "string",
            "title": "The Id Schema",
            "default": "",
            "examples": [
              "0078742000008"
            ],
            "pattern": "^(.{0,17})$"
          },
          "Address": {
            "$id": "#/properties/HeaderLocations/items/properties/Address",
            "type": "string",
            "title": "The Address Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.{0,30})$"
          },
          "City": {
            "$id": "#/properties/HeaderLocations/items/properties/City",
            "type": "string",
            "title": "The City Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.{0,30})$"
          },
          "State": {
            "$id": "#/properties/HeaderLocations/items/properties/State",
            "type": "string",
            "title": "The State Schema",
            "default": "",
            "examples": [
              "AZ",
              "NY"
            ],
            "pattern": "^([A-Za-z][A-Za-z])$"
          },
          "ZipCode": {
            "$id": "#/properties/HeaderLocations/items/properties/ZipCode",
            "type": "string",
            "title": "The Zipcode Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^([A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d|\d{5}(?:[-\s]\d{4})?)$"
          },
          "Country": {
            "$id": "#/properties/HeaderLocations/items/properties/Country",
            "type": "string",
            "title": "The Country Schema",
            "default": "",
            "examples": [
              "US",
              "CA"
            ],
            "pattern": "^([A-Za-z][A-Za-z][A-Za-z]|[A-Za-z][A-Za-z])$"
          }
        }
      }
    },
    "Equipment": {
      "$id": "#/properties/Equipment",
      "type": "object",
      "title": "The Equipment Schema",
      "required": [
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
          "pattern": "^(^$|.*)$"
        },
        "TrailerNumber": {
          "$id": "#/properties/Equipment/properties/TrailerNumber",
          "type": "string",
          "title": "The Trailernumber Schema",
          "default": "",
          "examples": [
            "90012"
          ],
          "pattern": "^(^$|.*)$"
        },
        "TrailerType": {
          "$id": "#/properties/Equipment/properties/TrailerType",
          "type": "string",
          "title": "The Trailertype Schema",
          "default": "",
          "examples": [
            "TF"
          ],
          "pattern": "^(^$|[A-Z]{2})$"
        },
        "TrailerSize": {
          "$id": "#/properties/Equipment/properties/TrailerSize",
          "type": "string",
          "title": "The Trailersize Schema",
          "default": "",
          "examples": [
            "5300"
          ],
          "pattern": "^(^$|\d{4})$"
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
              "StopCountry"
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
                "pattern": "^(\d+)$"
              },
              "StopType": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopType",
                "type": "string",
                "title": "The Stoptype Schema",
                "default": "",
                "examples": [
                  "SF"
                ],
                "pattern": "^(SF|SH|ST|CN)$"
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
                "pattern": "^([A-Za-z][A-Za-z])$"
              },
              "StopZip": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopZip",
                "type": "string",
                "title": "The Stopzip Schema",
                "default": "",
                "examples": [
                  "77523"
                ],
                "pattern": "^([A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d|\d{5}(?:[-\s]\d{4})?)$"
              },
              "StopCountry": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopCountry",
                "type": "string",
                "title": "The Stopcountry Schema",
                "default": "",
                "examples": [
                  "USA"
                ],
                "pattern": "^([A-Za-z][A-Za-z]|[A-Za-z][A-Za-z][A-Za-z])$"
              },
              "StopID": {
                "$id": "#/properties/Stops/items/properties/StopInfo/properties/StopID",
                "type": "string",
                "title": "The Stopid Schema",
                "default": "",
                "examples": [
                  "91515709"
                ],
                "pattern": "^(^$|.*)$"
              }
            }
          },
          "ContactInfo": {
            "$id": "#/properties/Stops/items/properties/ContactInfo",
            "type": "object",
            "title": "The Contactinfo Schema",
            "required": [
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
                "pattern": "^(^$|.*)$"
              },
              "Phone": {
                "$id": "#/properties/Stops/items/properties/ContactInfo/properties/Phone",
                "type": "string",
                "title": "The Phone Schema",
                "default": "",
                "examples": [
                  "5554561234"
                ],
                "pattern": "^(^$|.*)$"
              },
              "Email": {
                "$id": "#/properties/Stops/items/properties/ContactInfo/properties/Email",
                "type": "string",
                "title": "The Email Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(^$|.*)$"
              }
            }
          },
          "AppointmentInfo": {
            "$id": "#/properties/Stops/items/properties/AppointmentInfo",
            "type": "object",
            "title": "The Appointmentinfo Schema",
            "required": [
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
                "pattern": "^(^$|[0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9])$"
              },
              "EarlyTime": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/EarlyTime",
                "type": "string",
                "title": "The Earlytime Schema",
                "default": "",
                "examples": [
                  "2315"
                ],
                "pattern": "^(^$|[0-2][0-9][0-5][0-9])$"
              },
              "EarlyTimeZone": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/EarlyTimeZone",
                "type": "string",
                "title": "The Earlytimezone Schema",
                "default": "",
                "examples": [
                  "CT"
                ],
                "pattern": "^(^$|\D{2})$"
              },
              "LateDate": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateDate",
                "type": "string",
                "title": "The Latedate Schema",
                "default": "",
                "examples": [
                  "20190505"
                ],
                "pattern": "^(^$|[0-9][0-9][0-9][0-9][0-1][0-9][0-3][0-9])$"
              },
              "LateTime": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateTime",
                "type": "string",
                "title": "The Latetime Schema",
                "default": "",
                "examples": [
                  "2315"
                ],
                "pattern": "^(^$|[0-2][0-9][0-5][0-9])$"
              },
              "LateTimeZone": {
                "$id": "#/properties/Stops/items/properties/AppointmentInfo/properties/LateTimeZone",
                "type": "string",
                "title": "The Latetimezone Schema",
                "default": "",
                "examples": [
                  "CT"
                ],
                "pattern": "^(^$|\D{2})$"
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
                  "pattern": "^(^$|.{2,3})$"
                },
                "ReferenceNumber": {
                  "$id": "#/properties/Stops/items/properties/StopReferenceNumbers/items/properties/ReferenceNumber",
                  "type": "string",
                  "title": "The Referencenumber Schema",
                  "default": "",
                  "examples": [
                    "123456789"
                  ],
                  "pattern": "^(^$|.{1,17})$"
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
                  "pattern": "^(^$|.{1,20})$"
                },
                "PO": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/PO",
                  "type": "string",
                  "title": "The Po Schema",
                  "default": "",
                  "examples": [
                    "0815197030"
                  ],
                  "pattern": "^(^$|.{0,20})$"
                },
                "Pieces": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Pieces",
                  "type": "string",
                  "title": "The Pieces Schema",
                  "default": "",
                  "examples": [
                    "3"
                  ],
                  "pattern": "^(^$|\d{0,8})$"
                },
                "Weight": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Weight",
                  "type": "string",
                  "title": "The Weight Schema",
                  "default": "",
                  "examples": [
                    "5361"
                  ],
                  "pattern": "^(^$|\d{0,8})$"
                },
                "Volume": {
                  "$id": "#/properties/Stops/items/properties/OIDNumbers/items/properties/Volume",
                  "type": "string",
                  "title": "The Volume Schema",
                  "default": "",
                  "examples": [
                    "102"
                  ],
                  "pattern": "^(^$|\d{0,8})$"
                }
              }
            }
          }
        }
      }
    }
  }
}