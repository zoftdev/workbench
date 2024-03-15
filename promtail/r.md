actions:
  1:  # Action ID, can be any number or string
    action: delete_indices  # Specify the action to perform, e.g., delete_indices
    description: >-  # Description of the action
      Delete indices older than 30 days.
    options:  # Action-specific options
      ignore_empty_list: True  # Proceed with the action even if the list is empty after filtering
    filters:  # List of filters to apply
    - filtertype: pattern  # Filter by index name pattern
      kind: prefix  # Type of pattern, e.g., prefix, suffix, regex
      value: logstash-  # The pattern to match
    - filtertype: age  # Filter by index age
      source: creation_date  # Use index creation date to determine age
      direction: older  # Select indices older than the specified age
      unit: days  # Age unit, e.g., days, weeks, months
      unit_count: 30  # Age value in units