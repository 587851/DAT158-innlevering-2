from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    MSSubClass = SelectField('Type of dwelling', coerce=int, choices=[(20, '1-STORY 1946 & NEWER ALL STYLES'),(30, '1-STORY 1945 & OLDER'), (40, '1-STORY W/FINISHED ATTIC ALL AGES'),
    (45, '1-1/2 STORY - UNFINISHED ALL AGES'), (50, '1-1/2 STORY FINISHED ALL AGES'), (60, '2-STORY 1946 & NEWER'), (70, '2-STORY 1945 & OLDER'),
    (75, '2-1/2 STORY ALL AGES'), (80, 'SPLIT OR MULTI-LEVEL'), (85, 'SPLIT FOYER'), (90, 'DUPLEX - ALL STYLES AND AGES'), (120, '1-STORY PUD (Planned Unit Development) - 1946 & NEWER'), 
    (150, '1-1/2 STORY PUD - ALL AGES'), (160, '2-STORY PUD - 1946 & NEWER'), (180, 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER'), (190, 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER')])

    MSZoning = SelectField('The general zoning classification', coerce=int, choices=[(0, 'Commercial'), (1, 'Floating Village Residential'), (2, 'Residential High Density'), 
    (3, 'Residential Low Density'), (4, 'Residential Medium Density'), (5, 'Residential Low Density Park'), (6, 'Agriculture'), (7, 'Industrial')])

    LotArea = IntegerField('Lot size in square feet. Between 0 - 250,000 feet', validators=[NumberRange(min=0, max=250000)])
    Street = SelectField('Type of road access to property', coerce=int, choices=[(0, 'Gravel'),(1, 'Paved')])
    LotShape = SelectField('General shape of property', coerce=int, choices=[(0, 'Slightly irregular'),(1, 'Moderately Irregular'), (2, 'Irregular'), (3, 'Regular')])
    LandContour = SelectField('', coerce=int, choices=[(2, 'Depression'),(1, 'Hillside - Significant slope from side to side'), (0, 'Banked - Quick and significant rise from street grade to building'), (3, 'Near Flat/Level')])
    Utilities = SelectField('Type of utilities available', coerce=int, choices=[(0, 'All public Utilities (E,G,W,& S)'),(2, 'Electricity, Gas, and Water (Septic Tank)'), (1, 'Electricity and Gas Only'), (3, 'Electricity only')])
    LotConfig = SelectField('Lot configuration', coerce=int, choices=[(0, 'Corner lot'),(1, 'Cul-de-sac'), (2, 'Frontage on 2 sides of property'), (3, 'Frontage on 3 sides of property'), (4, 'Inside lot')])
    LandSlope = SelectField('Slope of property', coerce=int, choices=[(0, 'Gentle slope'),(1, 'Moderate Slope'), (2, 'Severe Slope')])

    Neighborhood =SelectField('Physical locations within Ames city limits', coerce=int, choices=[(0, 'Bloomington Heights'), (1, 'Bluestem'), (2, 'Briardale'), (3, 'Brookside'), (4, 'Clear Creek'),
    (5,'College Creek'), (6,'Crawford'), (7,'Edwards'), (8,'Gilbert'), (9,'Iowa DOT and Rail Road'), (10,'Meadow Village'), (11,'Mitchell'), (12,'North Ames'),
    (13,'Northridge'), (14,'Northpark Villa'), (15,'Northridge Heights'), (16,'Northwest Ames'), (17,'Old Town'), (18,'South & West of Iowa State University'), 
    (19,'Sawyer'), (20,'Sawyer West'), (21,'Somerset'), (22,'Stone Brook'), (23,'Timberland'), (24,'Veenker')])

    Condition1 = SelectField('Proximity to various conditions', coerce=int, choices=[(0, 'Adjacent to arterial street'),(1, 'Adjacent to feeder street'), (2, 'Normal'), (3, 'Within 200 of North-South Railroad'), 
    (4, 'Adjacent to North-South Railroad'),(5, 'Near positive off-site feature--park, greenbelt, etc.'), (6, 'Adjacent to postive off-site feature'), 
    (7, 'Within 200 of East-West Railroad'), (8, 'Adjacent to East-West Railroad')])
    Condition2 = SelectField('Proximity to various conditions', coerce=int, choices=[(0, 'Adjacent to arterial street'),(1, 'Adjacent to feeder street'), (2, 'Normal'), (3, 'Within 200 of North-South Railroad'), 
    (4, 'Adjacent to North-South Railroad'),(5, 'Near positive off-site feature--park, greenbelt, etc.'), (6, 'Adjacent to postive off-site feature'), 
    (7, 'Within 200 of East-West Railroad'), (8, 'Adjacent to East-West Railroad')])

    HouseStyle = SelectField('Style of dwelling ', coerce=int, choices=[(0, 'One and one-half story: 2nd level finished'),(1, 'One and one-half story: 2nd level unfinished'), 
    (2, 'One story'), (3, 'Two and one-half story: 2nd level finished'), (4, 'Two and one-half story: 2nd level unfinished'), (5, 'Two story'),(6, 'Split Foyer'), (7, 'Split Level')])

    OverallQual= IntegerField('Rates the overall material and finish of the house. Number between 1-10. 1 = Worst and 10 = Best', validators=[NumberRange(min=1, max=10)])
    OverallCond = IntegerField('Rates the overall condition of the house. Number between 1-10. 1 = Worst and 10 = Best', validators=[NumberRange(min=1, max=10)])

    YearBuilt = IntegerField('Original construction date. Between 1850 and 2010', validators=[NumberRange(min=1850, max=2010)])
    YearRemodAdd = IntegerField('Remodel date (same as construction date if no remodeling or additions)', validators=[NumberRange(min=1850, max=2010)])

    RoofStyle = SelectField('Type of roof', coerce=int, choices=[(0, 'Flat'),(1, 'Gable'), (2, 'Gabrel (Barn)'), (3, 'Hip'), (4, 'Mansard'), (5, 'Shed')])
    RoofMatl = SelectField('Roof material', coerce=int, choices=[(0, 'Clay or Tile'),(1, 'Standard (Composite) Shingle'), (2, 'Membrane '), (3, 'Metal'),
    (4, 'Roll'), (5, 'Gravel & Tar'), (6, 'Wood Shakes'), (7, 'Wood Shingles')])

    Exterior1st = SelectField('Exterior covering on house', coerce=int, choices=[(0, 'Asbestos Shingles'),(1, 'Asphalt Shingles'), (2, 'Brick Common'), 
    (3, 'Brick Face'), (4, 'Cinder Block'), (5, 'Cement Board'), (6, 'Hard Board'), (7, 'Imitation Stucco'), 
    (8, 'Metal Siding'),(9, 'Plywood'), (10, 'Stone'), (11, 'Stucco'),(12, 'Vinyl Siding'),(13, 'Wood Siding'), (14, 'Wood Shingles'), (15, 'Other'), (16, 'PreCast')])
    Exterior2nd = SelectField('', coerce=int, choices=[(0, 'Asbestos Shingles'),(1, 'Asphalt Shingles'), (2, 'Brick Common'), 
    (3, 'Brick Face'), (4, 'Cinder Block'), (5, 'Cement Board'), (6, 'Hard Board'), (7, 'Imitation Stucco'), 
    (8, 'Metal Siding'),(9, 'Other'), (10, 'Plywood'), (11, 'Stone'),(12, 'Stucco'),(13, 'Vinyl Siding'), (14, 'Wood Siding'), (15, 'Wood Shingles'), (16, 'PreCast')])

    #a = SelectField('', coerce=int, choices=[(0, ''),(1, ''), (2, ''), (3, '')])

    MasVnrType = SelectField('Masonry veneer type', coerce=int, choices=[(0, 'Brick Common'),(1, 'Brick Face'), (2, 'None '), (3, 'Stone'), (4, 'Cinder Block')])
    MasVnrArea = FloatField('Masonry veneer area in square feet. Between 0 and 2000', validators=[NumberRange(min=0, max=2000)])

    ExterQual= SelectField('Evaluates the quality of the material on the exterior ', coerce=int, choices=[(0, 'Excellent'),(2, 'Good'), (3, 'Average/Typical'), (1, 'Fair'), (4,'Poor')])
    ExterCond = SelectField('Evaluates the present condition of the material on the exterior', coerce=int, choices=[(0, 'Excellent'),(2, 'Good'), (4, 'Average/Typical'), (1, 'Fair'), (3,'Poor')])
    Foundation = SelectField('Type of foundation', coerce=int, choices=[(0, 'Brick & Tile'),(1, 'Cinder Block'), (2, 'Poured Contrete'), (3, 'Slab'), (4,'Stone'), (5, 'Wood')])

    BsmtFinSF1 = IntegerField('Type 1 finished square feet, Number between 0 and 6000', validators=[NumberRange(min=0, max=6000)])
    BsmtFinSF2 = IntegerField('Type 2 finished square feet, Number between 0 and 2000', validators=[NumberRange(min=0, max=2000)])
    BsmtUnfSF = IntegerField('Unfinished square feet of basement area, Number between 0 and 3000', validators=[NumberRange(min=0, max=3000)])
    TotalBsmtSF = IntegerField('Total square feet of basement area, Number between 0 and 7000', validators=[NumberRange(min=0, max=7000)])

    Heating = SelectField('Type of heating ', coerce=int, choices=[(0, 'Floor Furnace'),(1, 'Gas forced warm air furnace'), (2, 'Gas hot water or steam heat'), (3, 'Gravity furnace'), (4, 'Hot water or steam heat other than gas'), (5, 'Wall furnace')])
    HeatingQC = SelectField('Heating quality and condition', coerce=int, choices=[(0, 'Excellent'),(2, 'Good'), (4, 'Average/Typical'), (1, 'Fair'), (3, 'Poor')])
    CentralAir = SelectField('Central air conditioning', coerce=int, choices=[(0, 'No'),(1, 'Yes')])
    Electrical = SelectField('', coerce=int, choices=[(0, 'Fuse Box over 60 AMP and all Romex wiring (Average)'),(1, '60 AMP Fuse Box and mostly Romex wiring (Fair)'), 
    (2, '60 AMP Fuse Box and mostly knob & tube wiring (poor)'), (3, 'Mixed'), (4, 'Standard Circuit Breakers & Romex')])

    _1stFlrSF = IntegerField('First Floor square feet, Number between 100 and 6000', validators=[NumberRange(min=100, max=6000)])
    _2ndFlrSF = IntegerField('Second floor square fee, Number between 0 and 6000', validators=[NumberRange(min=0, max=6000)])
    LowQualFinSF = IntegerField('Low quality finished square feet (all floors), Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    
    GrLivArea = IntegerField('Above grade (ground) living area square feet, Number between 100 and 12000', validators=[NumberRange(min=100, max=12000)])
    BsmtFullBath = IntegerField('Basement full bathrooms, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    BsmtHalfBath = IntegerField('Basement half bathrooms, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    FullBath = IntegerField('Full bathrooms above grade, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    HalfBath= IntegerField('Half baths above grade, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    BedroomAbvGr = IntegerField('Bedrooms above grade (does NOT include basement bedrooms), Number between 0 and 10', validators=[NumberRange(min=0, max=10)])
    KitchenAbvGr = IntegerField('Kitchens above grade, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    KitchenQual = SelectField('Kitchen quality', coerce=int, choices=[(0, 'Excellent'), (2, 'Good'), (3, 'Typical/Average'), (1, 'Fair'), (4, 'Poor')])
    TotRmsAbvGrd = IntegerField('Total rooms above grade (does not include bathrooms),Number between 1 and 20', validators=[NumberRange(min=1, max=20)])
    Functional = SelectField('Home functionality (Assume typical unless deductions are warranted)', coerce=int, choices=[(0, 'Major Deductions 1'),(1, 'Major Deductions 2'), 
    (2, 'Minor Deductions 1'), (3, 'Minor Deductions 3'), (4, 'Moderate Deductions'), (5, 'Severely Damaged'), (6  , 'Typical Functionality'), (7, 'Salvage only')])
    Fireplaces = IntegerField('Number of fireplaces, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    GarageCars = IntegerField('Size of garage in car capacity, Number between 0 and 5', validators=[NumberRange(min=0, max=5)])
    GarageArea = IntegerField('Size of garage in square feet, Number between 0 and 1600', validators=[NumberRange(min=0, max=1600)])
    PavedDrive = SelectField('Paved driveway', coerce=int, choices=[(2, 'Paved'),(1, 'Partial Pavement'), (0, 'Dirt/Gravel')])
    WoodDeckSF = IntegerField('Wood deck area in square feet, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    OpenPorchSF = IntegerField('Open porch area in square feet, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    EnclosedPorch = IntegerField('Enclosed porch area in square feet, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    _3SsnPorch = IntegerField('Three season porch area in square feet, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    ScreenPorch = IntegerField('Screen porch area in square fee, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    PoolArea = IntegerField('Pool area in square feet, Number between 0 and 1000', validators=[NumberRange(min=0, max=1000)])
    MiscVal = IntegerField('Value of miscellaneous feature, Number between 0 and 18000', validators=[NumberRange(min=0, max=18000)])
    MoSold = IntegerField('Month Sold (MM), 1-12', validators=[NumberRange(min=1, max=12)]) 
    YrSold = IntegerField('Year Sold (YYYY), 2006-2010', validators=[NumberRange(min=2006, max=2010)])
    SaleType = SelectField('Type of sale', coerce=int, choices=[(0, 'Court Officer Deed/Estate'),(1, 'Warranty Deed - Cash'), (2, 'Contract 15% Down payment regular terms'), 
    (3, 'Contract Low Down'), (4, 'Contract Low Interest'),(5, 'Contract Low Down payment and low interest'), (6, 'Home just constructed and sold'), (7, 'other'), 
    (8, 'Warranty Deed - Conventional'),(9, 'Warranty Deed - VA Loan')])
    SaleCondition = SelectField('Condition of sale', coerce=int, choices=[(0, 'Abnormal Sale -  trade, foreclosure, short sale'),(1, 'Adjoining Land Purchase'), 
    (2, 'Allocation - two linked properties with separate deeds, typically condo with a garage unit'), (3, 'Sale between family members'), 
    (4, 'Normal Sale'), (5, 'Home was not completed when last assessed (associated with New Homes)')])


    submit = SubmitField('Submit')
