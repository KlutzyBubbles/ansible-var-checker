# ansible-var-checker

CLI to check what vars are defined / used to find undefined or extra vars not documented.

Based on source for ansible 2.9 and striped down and modified version of jinja2schema.

## Known Issues

- Sub attributes of a dictionary are marked as defined if a different sub attribute is set e.g

```yaml
# Setting
dict:
  sub: yay

# Will cause the use of the following undefined var to be marked as defined
{{ dict.undefined }}
```

- Setting variables in jinja2 templates are seen as variable usage and will be marked as undefined if they have not been registered outside of the jinja2 template
