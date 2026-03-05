def build_submission(business_name, industry, employee_count, broker_id,
                       *endorsements, coverage_tier='standard', **metadata):
    """Builds the calculated premium using raw data from the broker and
    performing some calculations."""
    metadata['business name'] = business_name
    metadata['industry'] = industry
    metadata['employee count'] = employee_count
    metadata['broker_id'] = broker_id
    metadata['endorsements'] = endorsements
    metadata['coverage tier'] = coverage_tier

    base_premium = calc_base_premium(metadata['industry'],
                                     metadata['employee count'],
                                     metadata['coverage tier'])
    
    updated_premium = apply_broker_discount(base_premium,
                                            metadata['broker_id'])
    
    calculated_premium = add_endorsement_costs(updated_premium,
                                               metadata['endorsements'])
    
    metadata['calculated premium'] = calculated_premium

    return metadata

def calc_base_premium(industry, employee_count, tier='standard'):
    """Calculates the base premium for each business."""
    if industry == 'logistics':
        base_rate = 410
    elif industry == 'healthcare':
        base_rate = 620
    elif industry == 'hospitality':
        base_rate = 390
    elif industry == 'technology':
        base_rate = 530
    elif industry == 'construction':
        base_rate = 710
    
    if tier == 'standard':
        tier_rate = 1.00
    elif tier == 'basic':
        tier_rate = 0.85
    elif tier == 'enhanced':
        tier_rate = 1.20
    
    base_premium = base_rate * employee_count * tier_rate
    return base_premium

def apply_broker_discount(base_premium, broker_id):
    """Applies a broker discount to the base premium when applicabale."""
    if broker_id == 'br-091':
        broker_discount = 1.00 - 0.08
    elif broker_id == 'br-204':
        broker_discount = 1.00 - 0.05
    elif broker_id == 'br-317':
        broker_discount = 1.00
    
    updated_premium = base_premium * broker_discount
    return updated_premium

def add_endorsement_costs(updated_premium, endorsements):
    """Applies endorsement costs to the updated premium."""
    endorsement_costs = 0
    if 'cyber' in endorsements:
        endorsement_costs += 1200
    if 'inland_marine' in endorsements:
        endorsement_costs += 850
    if 'umbrella' in endorsements:
        endorsement_costs += 2500
    if 'hired_auto' in endorsements:
        endorsement_costs += 600
    if 'employment_practices' in endorsements:
        endorsement_costs += 950
    
    calculated_premium = updated_premium + endorsement_costs
    return calculated_premium

def process_submissions(pending, quoted):
    """Processes submissions and moves a copy of them to a list of quoted
    submissions."""
    while pending:
        processing = pending.pop(0)
        print(f"Processing submission for {processing['business name'].title()}")
        quoted.append(processing)

def completed_submissions(quoted):
    """Prints the completed submissions and their calculated premium."""
    print("\nQuotes Calculated:")
    for quote in quoted:
        print(f"\n{quote['business name'].title()}: ${quote['calculated premium']}")
        if quote['endorsements']:
            print(f"\tEndorsements: {quote['endorsements']}")

def print_original(original_list):
    """Prints the original list to show it is unedited."""
    print(f"\npending_submissions still keeps an original copy.")
    print(f"\nAccounts still in pending_submissions")
    for submission in original_list:
        print(f"\t{submission['business name'].title()}")