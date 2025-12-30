# Recommendation-System-for-Anime-Movie

## Projects description

The rapid growth of online anime platforms has made effective content discovery increasingly challenging.
Users face an overwhelming number of choices, while feedback data remain sparse and noisy, complicating 
personalized recommendation. In addition, frequent introduction of new users and items leads to persistent
cold-start issues, and anime content often contains rich but heterogeneous information such as genres,
tags, and textual descriptions.

In this project, we study anime movie recommendation from a unified perspective that integrates item quality 
ranking, content-based recommendation, collaborative filtering. We first address the problem of item quality
estimation by framing it as a statistical inference task. Rather than relying solely on point estimates 
such as average ratings, we explore uncertainty-aware ranking methods based on bootstrap resampling, Bayesian
bootstrap, and Dirichlet posterior inference. These approaches enable more robust estimation of item quality 
under sparse and noisy user feedback.

Building on item quality ranking, we explore multiple recommendation paradigms. For content-based recommendation,
we develop models that utilize both categorical features (e.g., genres, studios, and tags) and textual descriptions
to capture semantic relationships between items and user preferences, particularly in cold-start scenarios. We
also investigate collaborative filtering approaches that learn latent user–item representations from interaction
data. These include classical matrix factorization methods such as Singular Value Decomposition (SVD), as well as
neural approaches like Neural Collaborative Filtering (NCF), which model complex, non-linear user–item interactions
for improved recommendation performance.

Data link: [raw-data](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020)


## Empirical Result

<img width="1208" height="709" alt="image" src="https://github.com/user-attachments/assets/dfada43f-4e91-4771-897f-1b3b0aa181c8" />

<img width="1209" height="337" alt="image" src="https://github.com/user-attachments/assets/6158ea16-8930-4d0c-9b12-04713624717d" />


