# Cloud platform practical checklist

Use this as a guided lab checklist for a cloud platform such as AWS, Microsoft Azure or Google Cloud.

## Before creating resources
- [ ] Sign in using your own authorized account.
- [ ] Enable multi-factor authentication where available.
- [ ] Set a budget alert and understand the pricing for the resources you plan to use.
- [ ] Choose a region and record why it is suitable.
- [ ] Never place credentials, API keys or personal information in source code or Git.

## Basic deployment plan
1. Package the application and pin its Python dependencies in `requirements.txt`.
2. Test it locally before uploading anything.
3. Select a service appropriate to the workload (VM, container service, managed notebook or ML platform).
4. Store secrets in the provider's secret manager or environment configuration.
5. Apply least-privilege access and restrict public network access.
6. Add logging and health checks.
7. Confirm a budget limit/alert and stop or delete resources after the lab.
8. Document the endpoint, access method and cleanup steps without exposing secrets.

## Reflection questions
1. What is the difference between IaaS, PaaS and SaaS?
2. Why should a cloud access key not be committed to GitHub?
3. What is the benefit of a budget alert?
4. Which service would you choose for a small batch prediction script, and why?

This checklist is a learning guide; it does not create or configure cloud resources.