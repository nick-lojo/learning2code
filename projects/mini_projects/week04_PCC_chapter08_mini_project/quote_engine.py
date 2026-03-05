import quote_helpers

# build_submission order of parameters: business_name, industry,
# employee_count, broker_id, *endorsements, coverage_tier='standard',
# **metadata

lakeside = quote_helpers.build_submission('lakeside freight llc',
                                                  'logistics', 42, 'br-091',
                                                  'cyber', 'inland_marine',
                                                  priority='high',
                                                  flagged=True)

mesa_verde = quote_helpers.build_submission('mesa verde clinic', 'healthcare',
                                            18, 'br-204', 'cyber', 'umbrella',
                                            'employment_practices',
                                            notes='renewal candidate')

thornwood = quote_helpers.build_submission('thornwood pub & grill',
                                           'hospitality', 11, 'br-091')

apex = quote_helpers.build_submission('apex data solutions', 'technology',
                                           63, 'br-317', 'cyber', 'umbrella',
                                           coverage_tier='enhanced',
                                           account_manager='Rivera')

ridgeline = quote_helpers.build_submission('ridgeline contractors inc',
                                          'construction', 29, 'br-204',
                                          'inland_marine', 'hired_auto',
                                          'umbrella', coverage_tier='basic',)

pending_submissions = [lakeside, mesa_verde, thornwood, apex, ridgeline]
quoted_submissions = []

quote_helpers.process_submissions(pending_submissions[:], quoted_submissions)

quote_helpers.completed_submissions(quoted_submissions)

quote_helpers.print_original(pending_submissions)